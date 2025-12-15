"""
Application configuration using pydantic-settings
"""

from pydantic_settings import BaseSettings
from pydantic import computed_field


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Gemini API
    gemini_api_key: str = ""
    
    # CORS - Railway uses ALLOWED_ORIGINS env var
    allowed_origins: str = "http://localhost:3000"
    
    @computed_field
    @property
    def cors_origins(self) -> list[str]:
        """Parse allowed origins from comma-separated string"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]
    
    class Config:
        env_file = ".env"
        extra = "ignore"


# Global settings instance
settings = Settings()
