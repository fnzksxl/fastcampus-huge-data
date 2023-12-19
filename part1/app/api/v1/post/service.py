from app import model


async def postUpload(data, db):
    row = model.Post(**data.dict())
    db.add(row)
    db.commit()

    return row.as_dict()
