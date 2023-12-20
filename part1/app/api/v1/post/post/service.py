from sqlalchemy import desc, or_
from app import model


async def postUpload(data, db):
    row = model.Post(**data.dict())
    db.add(row)
    db.commit()

    return row.as_dict()


async def postCount(id, firstDate, lastDate, db):
    row = (
        db.query(model.Post)
        .filter(model.Post.memberId == id, model.Post.created_at.between(firstDate, lastDate))
        .all()
    )

    return {"count": len(row), "posts": row}


async def postPage(memberId, offset, limit, db):
    start = offset * limit
    row = (
        db.query(model.Post)
        .filter_by(memberId=memberId)
        .order_by(desc(model.Post.created_at))
        .offset(start)
        .limit(limit)
        .all()
    )

    return row


async def postCursor(memberId, size, key, db, follow=None):
    async def findAllByMemberIdAndOrderByIdDesc(memberId, size, follow):
        if follow:
            return (
                db.query(model.Post)
                .filter(
                    or_(*[model.Post.memberId == member_id.toMemberId for member_id in memberId])
                )
                .order_by(desc(model.Post.id))
                .limit(size)
                .all()
            )

        else:
            return (
                db.query(model.Post)
                .filter_by(memberId=memberId)
                .order_by(desc(model.Post.id))
                .limit(size)
                .all()
            )

    async def findAllByLessThanKeyAndMemberIdAndOrderByIdDesc(memberId, key, size, follow):
        if follow:
            return (
                db.query(model.Post)
                .filter(
                    or_(*[model.Post.memberId == member_id.toMemberId for member_id in memberId]),
                    model.Post.id < key,
                )
                .order_by(desc(model.Post.id))
                .limit(size)
                .all()
            )
        else:
            return (
                db.query(model.Post)
                .filter(model.Post.memberId == memberId, model.Post.id < key)
                .order_by(desc(model.Post.id))
                .limit(size)
                .all()
            )

    if key:
        posts = await findAllByLessThanKeyAndMemberIdAndOrderByIdDesc(memberId, key, size, follow)
        return {"posts": posts, "nextKey": posts[-1].id if len(posts) else 0}
    else:
        posts = await findAllByMemberIdAndOrderByIdDesc(memberId, size, follow)
        return {"posts": posts, "nextKey": posts[-1].id if len(posts) else 0}
