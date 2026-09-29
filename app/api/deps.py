from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService


# TODO: replace with real dependency injection / lifespan state
_repository: PostRepository | None = None
_service: PostService | None = None


def get_repository() -> PostRepository:
    raise NotImplementedError


def get_service() -> PostService:
    raise NotImplementedError
