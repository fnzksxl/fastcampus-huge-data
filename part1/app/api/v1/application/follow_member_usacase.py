from app.api.v1.member.service import memberSearch
from app.api.v1.follow.service import followCreate


async def follow_member_usacase(fromMemberId, toMemberId, db):
    """
    --- 목표 ---
      1. 입력받은 memberId 회원 조회
      2. Follow Service로 create
    """

    fromMember = await memberSearch(fromMemberId, db)
    toMember = await memberSearch(toMemberId, db)

    follow = await followCreate(fromMember, toMember, db)

    return follow
