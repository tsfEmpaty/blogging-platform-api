from datetime import datetime, timezone

from app.models import PostCreate, PostResponse
from app.models.post import Post
from app.repositories.post_repository import PostRepository


def _format_datetime(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def _to_response(post: Post) -> PostResponse:
    return PostResponse(
        id=post.id,
        title=post.title,
        content=post.content,
        category=post.category,
        tags=[tag for tag in post.tags.split(",") if tag],
        createdAt=_format_datetime(post.created_at),
        updatedAt=_format_datetime(post.updated_at),
    )


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    async def create_post(self, post: PostCreate) -> PostResponse:
        db_post = await self.repository.create(post)
        return _to_response(db_post)

    async def get_posts(self, term: str | None = None) -> list[PostResponse]:
        db_posts = await self.repository.get_all(term)
        return [_to_response(p) for p in db_posts]

    async def get_post(self, post_id: int) -> PostResponse | None:
        db_post = await self.repository.get_by_id(post_id)
        if db_post is None:
            return None
        return _to_response(db_post)

    async def update_post(self, post_id: int, post: PostCreate) -> PostResponse | None:
        db_post = await self.repository.update(post_id, post)
        if db_post is None:
            return None
        return _to_response(db_post)

    async def delete_post(self, post_id: int) -> bool:
        return await self.repository.delete(post_id)
