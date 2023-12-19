from datetime import datetime
from pydantic import BaseModel


class memberUpdate(BaseModel):
    nickname: str


class memberRegister(memberUpdate):
    email: str
    birthday: datetime


class memberFind(memberRegister):
    id: int


class nicknameHistory(BaseModel):
    nickname: str
    memberId: int
    id: int
    created_at: datetime
