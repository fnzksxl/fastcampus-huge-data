from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api.v1.application.follow_member_usacase import follow_member_usacase
from app.api.v1.application.get_members_from_follow_usacase import get_members_from_follow_usacase
from app.api.v1.follow.schema import FollowReturn
from app.database import get_db


router = APIRouter(tags=["Follow"])


@router.post("/{fromMemberId}/{toMemberId}", status_code=201, response_model=FollowReturn)
async def create(fromMemberId: int, toMemberId: int, db: Session = Depends(get_db)):
    return await follow_member_usacase(fromMemberId, toMemberId, db)


@router.get("/{memberId}", status_code=200)
async def find(memberId: int, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. fromMemberId로 Follow List 받아오기
    """
    return await get_members_from_follow_usacase(memberId, db)
