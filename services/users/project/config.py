from pydantic import BaseSettings
import os
from functools import lru_cache

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    env_name: str = "Dev"
    base_url: str = "http://localhost:8000"
    db_url: str = os.environ.get("db_url")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings: {settings.env_name}")
    return settings