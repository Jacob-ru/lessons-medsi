from functools import lru_cache

from pydantic import BaseSettings


class APPSettings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool
    VERSION: str = "1.0"
    API_ROOT_PATH = ''
    API_ROUTE = ''
    SECRET_KEY: str
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60

    class Config:
        env_file = ".env.example"


@lru_cache()
def get_app_settings() -> APPSettings:
    return APPSettings()
