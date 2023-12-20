from app.api.v1.follow.service import findAllByMemberId
from app.api.v1.post.post.service import postCursor


async def get_timeline_post_usacase(memberId, key, size, db):
    """
    1. memberId -> follow 조회
    2. 1번 결과로 게시물 조회
    """
    memberIds = await findAllByMemberId(memberId, db)
    if len(memberIds):
        return await postCursor(memberIds, key, size, db, True)
    else:
        return {"posts": [], "nextKey": 0}
