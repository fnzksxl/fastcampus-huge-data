from app import model


async def timelineUpload(postId, followingIds, db):
    data = [
        model.Timeline(postId=postId, memberId=following.toMemberId) for following in followingIds
    ]

    db.bulk_insert_mappings(model.Timeline, [timeline.__dict__ for timeline in data])
    db.commit()
