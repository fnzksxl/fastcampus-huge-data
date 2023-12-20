from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.database import get_db
from app.api.v1.application.post_fanout_usacase import post_fanout_usacase
from app.api.v1.application.get_timeline_post_usacase import get_timeline_post_usacase
from app.api.v1.post.post.schema import PostUpload, PostReturn
from app.api.v1.post.post.service import postUpload, postCount, postPage, postCursor

router = APIRouter(tags=["Post"])


@router.post("", status_code=201, response_model=PostReturn)
async def create(data: PostUpload, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 게시글(회원식별 ID, 내용)을 등록한다.
    ------------

    --- 바디 ---
    1. PostUpload
    - memberId: int
    - content: str
    ------------
    """
    return await postUpload(data, db)


@router.get("/{memberId}", status_code=200)
async def count(memberId: int, firstDate: date, lastDate: date, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 주어진 일자 내의 게시물 개수를 반환한다.
    ------------

    --- Path 파라미터 ---
    1. memberId: int
    --------------------

    --- Query 파라미터 ---
    1. firstDate: date
    2. lastDate: date
    ---------------------
    """
    return await postCount(memberId, firstDate, lastDate, db)


@router.get("/page/{memberId}", status_code=200)
async def page(memberId: int, offset: int, limit: int, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. memberId가 memberId인 게시글을 가져온 후
    2. (offset*limit)번 째 게시글부터 (offset*limit)+limit번 째 게시글을 가져와 반환한다.
    ------------

    --- Path 파라미터 ---
    1. memberId: int
    --------------------

    --- Qeury 파라미터 ---
    1. offset: int
    2. limit: int
    ---------------------
    """
    return await postPage(memberId, offset, limit, db)


@router.get("/cursor/{memberId}", status_code=200)
async def cursor(memberId: int, size: int, key: int = None, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. memberId 가 memberId인 게시글을 가져온 후
    2. id가 key보다 작은 게시글을 size 개수 만큼 가져와 반환한다.
    ------------

    --- Path 파라미터 ---
    1. memberId: int
    --------------------

    --- Query 파라미터 ---
    1. size: int
    2. key: int (can be None)
    ---------------------
    """
    return await postCursor(memberId, size, key, db)


@router.get("/cursor/timeline/{memberId}", status_code=200)
async def cursorFollowTimeline(
    memberId: int, size: int, key: int = None, db: Session = Depends(get_db)
):
    """
    --- 목표 ---
    1. memberId를 가진 member의 follow 리스트를 받는다
    2. 1의 결과로 id가 key보다 작은 게시글을 size 개수만큼 가져와 반환한다.
    ------------

    --- Path 파라미터 ---
    1. memberId: int
    --------------------

    --- Query 파라미터 ---
    1. size: int
    2. key: int (can be None)
    ---------------------
    """
    return await get_timeline_post_usacase(memberId, size, key, db)


@router.post("/fanout", status_code=201)
async def createFanout(data: PostUpload, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. 게시글을 등록하고, 타임라인에 추가한다.
    ------------

    --- 바디 ---
    1. PostUpload
    - memberId: int
    - content: str
    ------------
    """
    return await post_fanout_usacase(data, db)
