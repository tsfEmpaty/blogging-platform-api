from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Blogging Platform API"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


settings = Settings()
