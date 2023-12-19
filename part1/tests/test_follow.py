import pytest


@pytest.mark.asyncio
async def test_follow_create(client, user, user2):
    r = await client.post(f"/follow/{user.id}/{user2.id}")
    data = r.json()

    assert r.status_code == 201
    assert data.get("fromMemberId") == user.id
    assert data.get("toMemberId") == user2.id


@pytest.mark.asyncio
async def test_follow_get(client, user, user2):
    await client.post(f"/follow/{user.id}/{user2.id}")
    r = await client.get(f"/follow/{user.id}")
    data = r.json()

    assert r.status_code == 200
    assert data[0].get("id") == user2.id
