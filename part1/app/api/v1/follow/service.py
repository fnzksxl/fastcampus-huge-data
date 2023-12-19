from app import model


async def followCreate(fromMember, toMember, db):
    assert fromMember["id"] != toMember["id"], "from, to 회원이 동일합니다."

    row = model.Follow(fromMemberId=fromMember["id"], toMemberId=toMember["id"])
    db.add(row)
    db.commit()

    return row.as_dict()
