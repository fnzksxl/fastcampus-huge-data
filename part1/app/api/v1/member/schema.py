from datetime import datetime
from pydantic import BaseModel


class memberRegister(BaseModel):
    email: str
    nickname: str
    birthday: datetime


class memberFind(memberRegister):
    id: int
