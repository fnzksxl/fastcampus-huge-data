import pytest_asyncio
from datetime import datetime
from httpx import AsyncClient

from app import main, model
from app.database import engine, get_db
from app.config import settings


@pytest_asyncio.fixture(scope="session")
def app():
    if not settings.TESTING:
        raise SystemError("TESTING environment must be set true")

    return main.app


@pytest_asyncio.fixture
async def session():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@pytest_asyncio.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test/api/v1") as ac:
        model.Base.metadata.drop_all(bind=engine)
        model.Base.metadata.create_all(bind=engine)

        yield ac


@pytest_asyncio.fixture
def user(session) -> model.Member:
    row = model.Member(nickname="samplename", email="sample@sample.com", birthday=datetime.now())
    session.add(row)
    session.commit()

    return row
