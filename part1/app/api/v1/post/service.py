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
