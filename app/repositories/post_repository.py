from app.models import PostCreate


class PostRepository:
    def create(self, post: PostCreate) -> dict:
        raise NotImplementedError

    def get_all(self, term: str | None = None) -> list[dict]:
        raise NotImplementedError

    def get_by_id(self, post_id: int) -> dict | None:
        raise NotImplementedError

    def update(self, post_id: int, post: PostCreate) -> dict | None:
        raise NotImplementedError

    def delete(self, post_id: int) -> bool:
        raise NotImplementedError
