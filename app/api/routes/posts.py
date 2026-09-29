from fastapi import APIRouter

from app.models import PostCreate

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post(path="/")
def create_post(post: PostCreate):
    raise NotImplementedError


@router.get(path="")
def get_posts(term: str | None = None):
    raise NotImplementedError


@router.get(path="/{post_id}")
def get_post(post_id: int):
    raise NotImplementedError


@router.put(path="/{post_id}")
def update_post(post_id: int, post: PostCreate):
    raise NotImplementedError


@router.delete(path="/{post_id}")
def delete_post(post_id: int):
    raise NotImplementedError
