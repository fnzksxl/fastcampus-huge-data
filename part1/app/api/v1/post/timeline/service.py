from app import model


async def timelineUpload(postId, memberIds, db):
    data = [model.Timeline(postId=postId, memberId=member.fromMemberId) for member in memberIds]

    db.bulk_insert_mappings(model.Timeline, [timeline.__dict__ for timeline in data])
    db.commit()
