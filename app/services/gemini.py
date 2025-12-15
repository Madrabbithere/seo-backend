"""
Gemini AI service for SEO brief generation
"""

import json
import logging
from google import genai
from google.genai import types

from app.core.config import settings
from app.core.prompts import SEO_BRIEF_PROMPT
from app.schemas.brief import SEOBrief

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
    ) -> SEOBrief:
        """
        Generate an SEO brief using Gemini API
        
        Args:
            title: The content title/topic
            target_audience: Description of target audience
            primary_keywords: List of primary keywords
            secondary_keywords: List of secondary keywords
            
        Returns:
            SEOBrief: The generated SEO brief
            
        Raises:
            Exception: If API call fails or response parsing fails
        """
        # Format the prompt
        prompt = SEO_BRIEF_PROMPT.format(
            title=title,
            target_audience=target_audience,
            primary_keywords=", ".join(primary_keywords),
            secondary_keywords=", ".join(secondary_keywords) if secondary_keywords else "None specified"
        )
        
        try:
            # Generate content using the new SDK
            response = self.client.models.generate_content(
                model=self._model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    top_p=0.9,
                    max_output_tokens=2048,
                )
            )
            
            # Parse the JSON response
            response_text = response.text
            
            # Clean up response if it has markdown code blocks
            if response_text.startswith("```"):
                response_text = response_text.strip("```").strip()
                if response_text.startswith("json"):
                    response_text = response_text[4:].strip()
            
            # Parse JSON
            brief_data = json.loads(response_text)
            
            # Validate and return as Pydantic model
            return SEOBrief(**brief_data)
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Gemini response as JSON: {e}")
            logger.error(f"Response text: {response_text[:500]}")
            raise ValueError(f"Failed to parse AI response: {e}")
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            raise


# Singleton instance - client initialized lazily on first use
gemini_service = GeminiService()
