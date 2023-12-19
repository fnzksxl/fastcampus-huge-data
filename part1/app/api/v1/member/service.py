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
    await validateNickname(memberInfo.nickname)
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
    --- Update Nickname ---
    update member
    set nickname = : newName
    where id = : id;
    -----------------------

    ---------------- Save Nickname History ------------------
    insert into member_nickname_history (member_id, nickname)
    select id, nickname from member where id = :id;
    ----------------------------------------------------------

    """
    try:
        await validateNickname(newName)
        memberRow = db.query(model.Member).filter_by(id=id).first()
        try:
            # 강의에서는 바뀐 이름을 저장했지만, 나는 바뀌기 전 이름을 저장해보기로 했다.
            historyRow = model.MemberNicknameHistory(memberId=id, nickname=memberRow.nickname)
            db.add(historyRow)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"{e} Occured. While saving 'memberNicknameHistory",
            )
        memberRow.nickname = newName
        db.commit()

        return memberRow.as_dict()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While doing 'memberUpdateNickname'",
        )


async def memberGetNicknameHistories(memberId, db):
    """
    select * from member_nickname_history
    where member_id = : member_id
    """
    try:
        histories = db.query(model.MemberNicknameHistory).filter_by(memberId=memberId).all()
        return [history.as_dict() for history in histories]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"{e} Occured. While doing 'memberGetNicknameHistories'",
        )
