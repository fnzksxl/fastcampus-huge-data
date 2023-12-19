from pydantic import BaseModel


class FollowReturn(BaseModel):
    id: int
    fromMemberId: int
    toMemberId: int
