"""
Application configuration using pydantic-settings
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Gemini API
    gemini_api_key: str = ""
    
    # CORS
    allowed_origins_str: str = "http://localhost:3000"
    
    @property
    def allowed_origins(self) -> list[str]:
        """Parse allowed origins from comma-separated string"""
        return [origin.strip() for origin in self.allowed_origins_str.split(",")]
    
    class Config:
        env_file = ".env"
        extra = "ignore"


# Global settings instance
settings = Settings()
