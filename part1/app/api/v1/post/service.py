from sqlalchemy import desc
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
