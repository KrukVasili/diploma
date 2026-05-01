from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Sociolinguistic Adaptation System"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/data.db"
    MAX_TEXT_LENGTH: int = 1000
    API_PREFIX: str = "/api"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
