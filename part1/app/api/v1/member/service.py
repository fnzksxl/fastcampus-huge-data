from fastapi import HTTPException, status

from app import model


async def memberSave(memberInfo, db):
    try:
        assert len(memberInfo.nickname) < 10, "닉네임 최대 길이를 초과했습니다."
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While asserting 'memberSave'",
        )
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
