"""
Gemini AI service for SEO brief generation
"""

import logging
from google import genai
from google.genai import types

from app.core.config import settings
from app.core.prompts import SEO_BRIEF_PROMPT

logger = logging.getLogger(__name__)


class GeminiService:
    """Service for interacting with Google Gemini API"""
    
    _client = None
    _model = "gemini-2.5-flash"
    
    @property
    def client(self):
        """Lazy initialization of Gemini client"""
        if self._client is None:
            if not settings.gemini_api_key:
                raise ValueError("GEMINI_API_KEY environment variable is not set")
            self._client = genai.Client(api_key=settings.gemini_api_key)
        return self._client
    
    async def generate_brief(
        self,
        title: str,
        target_audience: str,
        primary_keywords: list[str],
        secondary_keywords: list[str]
    ) -> str:
        """
        Generate an SEO brief using Gemini API
        
        Args:
            title: The content title/topic
            target_audience: Description of target audience
            primary_keywords: List of primary keywords
            secondary_keywords: List of secondary keywords
            
        Returns:
            str: The generated SEO brief as plain text
            
        Raises:
            Exception: If API call fails
        """
        # Format the prompt
        prompt = SEO_BRIEF_PROMPT.format(
            title=title,
            target_audience=target_audience,
            primary_keywords=", ".join(primary_keywords),
            secondary_keywords=", ".join(secondary_keywords) if secondary_keywords else "None specified"
        )
        
        try:
            # Generate content using the SDK
            response = self.client.models.generate_content(
                model=self._model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    top_p=0.9,
                    max_output_tokens=2048,
                )
            )
            
            # Return the plain text response directly
            return response.text
            
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            raise


# Singleton instance - client initialized lazily on first use
gemini_service = GeminiService()
