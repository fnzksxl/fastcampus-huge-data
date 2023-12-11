from datetime import datetime
from pydantic import BaseModel


class memberUpdate(BaseModel):
    nickname: str


class memberRegister(memberUpdate):
    email: str
    birthday: datetime


class memberFind(memberRegister):
    id: int
