from pydantic import BaseModel


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list[str]
    createdAt: str
    updatedAt: str
