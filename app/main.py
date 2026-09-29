from fastapi import FastAPI

from app.api.routes.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8000, reload=True)
