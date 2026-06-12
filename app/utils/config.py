from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    """
    Application configuration class for loading environment variables using Pydantic Settings.

    Fields:
        app_name (str): The name of the application.
        owner (str): Owner/maintainer of the application.
        email (str): Contact email.
    """

    # model_config = SettingsConfigDict(env_file=str(env_path), extra="ignore")

    # Static App Info
    app_name: str = "Retrievel Augmented Generation"
    owner: str = "Thrishnav"
    email: str = "thrishnavai@gmail.com"

    openai_key: str
       
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> AppSettings:
    """
    Returns a singleton instance of AppSettings loaded from the .env file.
    Uses LRU caching to prevent reloading on each access.

    Returns:
        AppSettings: A cached instance of the configuration object.
    """
    return AppSettings()

# if __name__ == "__main__":
#     settings = get_settings()
#     print(settings.model_dump())