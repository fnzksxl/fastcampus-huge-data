from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api.v1.application.follow_member_usacase import follow_member_usacase
from app.api.v1.follow.schema import FollowReturn
from app.database import get_db


router = APIRouter(tags=["Follow"])


@router.post("/{fromMemberId}/{toMemberId}", status_code=201, response_model=FollowReturn)
async def create(fromMemberId: int, toMemberId: int, db: Session = Depends(get_db)):
    return await follow_member_usacase(fromMemberId, toMemberId, db)
