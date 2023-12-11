from fastapi import HTTPException, status

from app import model


async def validateNickname(nickname):
    try:
        assert len(nickname) < 10, "닉네임 최대 길이를 초과했습니다."
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While asserting 'memberSave'",
        )


async def memberSave(memberInfo, db):
    validateNickname(memberInfo.nickname)
    try:
        memberInfoRow = model.Member(**memberInfo.dict())
        db.add(memberInfoRow)
        db.commit()

        return memberInfoRow.as_dict()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While doing 'memberSave'",
        )


async def memberSearch(id, db):
    """
    select *
    from member where id = : id
    """
    try:
        memberRow = db.query(model.Member).filter_by(id=id).first()

        return memberRow.as_dict()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{e} Occured. While doing 'memberSearch"
        )


async def memberUpdateNickname(id, newName, db):
    """
    update member
    set nickname = : newName
    where id = : id;
    """
    try:
        memberRow = db.query(model.Member).filter_by(id=id).first()
        memberRow.nickname = newName
        db.commit()

        return memberRow.as_dict()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While doing 'memberUpdateNickname'",
        )
