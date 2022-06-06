from pydantic import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "hhtp://localhost:8000"
    db_url: str = os.environ.get("db_url")

def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings