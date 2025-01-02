"""
Application configuration settings.
Handles environment variables and configuration settings for the application.
"""
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    All settings must be provided in .env file - application will fail if any are missing.
    """
    # Version
    VERSION: str
    
    # Database settings
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    
    # Security settings
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # Environment settings
    ENVIRONMENT: str  # development/staging/production
    
    @property
    def DATABASE_URL(self) -> str:
        """Constructs PostgreSQL connection URL from settings"""
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    
    Raises:
        ValidationError: If any required setting is missing from .env
    """
    return Settings() 