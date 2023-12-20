from sqlalchemy import desc
from app import model


async def timelineUpload(postId, memberIds, db):
    data = [model.Timeline(postId=postId, memberId=member.fromMemberId) for member in memberIds]

    db.bulk_insert_mappings(model.Timeline, [timeline.__dict__ for timeline in data])
    db.commit()


async def timelineFind(memberId, size, key, db):
    async def findAllByMemberIdAndOrderByIdDesc(memberId, size):
        return (
            db.query(model.Timeline)
            .filter_by(memberId=memberId)
            .order_by(desc(model.Timeline.id))
            .limit(size)
            .all()
        )

    async def findAllByLessThanKeyAndMemberIdAndOrderByIdDesc(memberId, key, size):
        return (
            db.query(model.Post)
            .filter(model.Post.memberId == memberId, model.Timeline.id < key)
            .order_by(desc(model.Timeline.id))
            .limit(size)
            .all()
        )

    if key:
        posts = await findAllByLessThanKeyAndMemberIdAndOrderByIdDesc(memberId, key, size)
        return {"posts": posts, "nextKey": posts[-1].id if len(posts) else 0}
    else:
        posts = await findAllByMemberIdAndOrderByIdDesc(memberId, size)
        return {"posts": posts, "nextKey": posts[-1].id if len(posts) else 0}
