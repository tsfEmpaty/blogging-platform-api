from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import PostCreate
from app.models.post import Post


class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, post: PostCreate) -> Post:
        db_post = Post(
            title=post.title,
            content=post.content,
            category=post.category,
            tags=",".join(post.tags) if post.tags else "",
        )
        self.session.add(db_post)
        await self.session.commit()
        await self.session.refresh(db_post)
        return db_post

    async def get_all(self, term: str | None = None) -> list[Post]:
        query = select(Post)
        if term:
            pattern = f"%{term}%"
            query = query.where(
                or_(
                    Post.title.ilike(pattern),
                    Post.content.ilike(pattern),
                    Post.category.ilike(pattern),
                )
            )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_by_id(self, post_id: int) -> Post | None:
        result = await self.session.execute(select(Post).where(Post.id == post_id))
        return result.scalar_one_or_none()

    async def update(self, post_id: int, post: PostCreate) -> Post | None:
        db_post = await self.get_by_id(post_id)
        if db_post is None:
            return None
        db_post.title = post.title
        db_post.content = post.content
        db_post.category = post.category
        db_post.tags = ",".join(post.tags) if post.tags else ""
        await self.session.commit()
        await self.session.refresh(db_post)
        return db_post

    async def delete(self, post_id: int) -> bool:
        db_post = await self.get_by_id(post_id)
        if db_post is None:
            return False
        await self.session.delete(db_post)
        await self.session.commit()
        return True
