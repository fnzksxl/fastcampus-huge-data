from app.api.v1.follow.service import findAllByMemberId
from app.api.v1.post.post.service import postUpload
from app.api.v1.post.timeline.service import timelineUpload


async def post_fanout_usacase(data, db):
    post = await postUpload(data, db)
    memberIds = await findAllByMemberId(data.memberId, db)
    await timelineUpload(post["id"], memberIds, db)

    return post
