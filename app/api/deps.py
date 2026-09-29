from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal
from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


def get_repository(session: AsyncSession = Depends(get_db)) -> PostRepository:
    return PostRepository(session)


def get_service(
    repository: PostRepository = Depends(get_repository),
) -> PostService:
    return PostService(repository)
