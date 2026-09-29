from app.models import PostCreate
from app.repositories.post_repository import PostRepository


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def create_post(self, post: PostCreate) -> dict:
        raise NotImplementedError

    def get_posts(self, term: str | None = None) -> list[dict]:
        raise NotImplementedError

    def get_post(self, post_id: int) -> dict:
        raise NotImplementedError

    def update_post(self, post_id: int, post: PostCreate) -> dict:
        raise NotImplementedError

    def delete_post(self, post_id: int) -> None:
        raise NotImplementedError
