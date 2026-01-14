from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Supabase Configuration
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    
    # Server Configuration
    SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()