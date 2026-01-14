from supabase import create_client, Client
from config.settings import settings
import logging

logger = logging.getLogger(__name__)


class SupabaseDB:
    """Singleton class for Supabase database connection"""
    _instance: Client = None
    
    @classmethod
    def get_client(cls) -> Client:
        """
        Get or create Supabase client instance
        
        Returns:
            Client: Supabase client for database operations
        """
        if cls._instance is None:
            try:
                cls._instance = create_client(
                    supabase_url=settings.SUPABASE_URL,
                    supabase_key=settings.SUPABASE_KEY
                )
                logger.info("✅ Successfully connected to Supabase")
            except Exception as e:
                logger.error(f"❌ Failed to connect to Supabase: {str(e)}")
                raise
        
        return cls._instance

# Create a function to get the client (FastAPI dependency)
def get_supabase_client() -> Client:
    """FastAPI dependency to get Supabase client"""
    return SupabaseDB.get_client()