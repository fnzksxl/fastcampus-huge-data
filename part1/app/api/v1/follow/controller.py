from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from app.api.v1.application.follow_member_usacase import follow_member_usacase
from app.api.v1.follow.service import findAllByMemberId
from app.api.v1.follow.schema import FollowReturn
from app.database import get_db


router = APIRouter(tags=["Follow"])


@router.post("/{fromMemberId}/{toMemberId}", status_code=201, response_model=FollowReturn)
async def create(fromMemberId: int, toMemberId: int, db: Session = Depends(get_db)):
    return await follow_member_usacase(fromMemberId, toMemberId, db)


@router.get("/{memberId}", status_code=200, response_model=List[FollowReturn])
async def find(memberId: int, db: Session = Depends(get_db)):
    """
    --- 목표 ---
    1. fromMemberId로 Follow List 받아오기
    """
    return await findAllByMemberId(memberId, db)
