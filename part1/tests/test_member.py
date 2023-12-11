import pytest
import json


@pytest.mark.asyncio
async def test_get_user(client, user):
    r = await client.get(f"/member/{user.id}")
    data = r.json()

    assert r.status_code == 200
    assert data.get("nickname") == user.nickname


@pytest.mark.asyncio
async def test_post_user(client):
    body = {
        "email": "sample2@sample.com",
        "nickname": "sample2",
        "birthday": "2023-12-11T08:29:11.937Z",
    }

    r = await client.post("/member", data=json.dumps(body))
    data = r.json()

    assert r.status_code == 201
    assert data.get("nickname") == body["nickname"]


@pytest.mark.asyncio
async def test_put_user(client, user):
    body = {"nickname": "newNick"}
    r = await client.put(f"/member/{user.id}", data=json.dumps(body))
    data = r.json()

    assert r.status_code == 202
    assert data.get("nickname") == body["nickname"]
