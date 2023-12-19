from datetime import datetime, timedelta
import pytest
import json


@pytest.mark.asyncio
async def test_post_create(client, user):
    body = {"memberId": user.id, "content": "test content"}
    r = await client.post("/post", data=json.dumps(body))
    data = r.json()

    assert r.status_code == 201
    assert data.get("content") == body["content"]


@pytest.mark.asyncio
async def test_post_count(client, user, post):
    today = datetime.now()
    firstDate = (today - timedelta(days=1)).strftime("%Y-%m-%d")
    lastDate = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    r = await client.get(f"/post/{user.id}?firstDate={firstDate}&lastDate={lastDate}")
    data = r.json()

    assert r.status_code == 200
    assert data.get("posts")[0]["content"] == post.content
