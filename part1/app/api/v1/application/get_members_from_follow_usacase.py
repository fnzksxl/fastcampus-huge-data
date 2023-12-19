from app.api.v1.member.service import memberSearch
from app.api.v1.member.schema import memberFind
from app.api.v1.follow.service import findAllByMemberId


async def get_members_from_follow_usacase(memberId, db):
    followList = await findAllByMemberId(memberId, db)
    followingList = []
    for following in followList:
        followingList.append(memberFind(**await memberSearch(following.id, db)))

    return followingList
