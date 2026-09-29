import pytest
import pytest_asyncio
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.api.deps import get_db, get_repository, get_service
from app.core.database import Base
from app.main import app
from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session


def override_get_repository(
    session: AsyncSession = Depends(override_get_db),
) -> PostRepository:
    return PostRepository(session)


def override_get_service(
    repository: PostRepository = Depends(override_get_repository),
) -> PostService:
    return PostService(repository)


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_repository] = override_get_repository
    app.dependency_overrides[get_service] = override_get_service
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    app.dependency_overrides.clear()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
