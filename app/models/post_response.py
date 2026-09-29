from datetime import datetime

from pydantic import ConfigDict

from .post_create import PostCreate


class PostResponse(PostCreate):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    createdAt: datetime
    updatedAt: datetime
