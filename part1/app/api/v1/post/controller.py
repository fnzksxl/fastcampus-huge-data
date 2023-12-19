from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.database import get_db
from app.api.v1.post.schema import PostUpload, PostReturn
from app.api.v1.post.service import postUpload, postCount

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
