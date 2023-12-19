# PostUpload, PostReturn
from pydantic import BaseModel


class PostUpload(BaseModel):
    content: str
    memberId: int


class PostReturn(PostUpload):
    id: int
