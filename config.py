from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Excel Upload"
    DATABASE_URL: str = "sqlite:///test.db"
    class Config:
        case_sensitive = True

settings = Settings() 