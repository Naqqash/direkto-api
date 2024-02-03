from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str
    access_token_expire_minutes: int
    database_url: str
    origins: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
