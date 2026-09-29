from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Blogging Platform API"
    host: str = "localhost"
    port: int = 8000
    database_url: str = "sqlite+aiosqlite:///./blogging.db"


settings = Settings()
