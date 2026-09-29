from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.api.deps import get_db, get_repository, get_service
from app.models import PostCreate, PostResponse
from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("", status_code=HTTP_201_CREATED, response_model=PostResponse)
async def create_post(
    post: PostCreate,
    service: PostService = Depends(get_service),
):
    return await service.create_post(post)


@router.get("", response_model=list[PostResponse])
async def get_posts(
    term: str | None = None,
    service: PostService = Depends(get_service),
):
    return await service.get_posts(term)


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(
    post_id: int,
    service: PostService = Depends(get_service),
):
    db_post = await service.get_post(post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int,
    post: PostCreate,
    service: PostService = Depends(get_service),
):
    db_post = await service.update_post(post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    service: PostService = Depends(get_service),
):
    deleted = await service.delete_post(post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return None
