"""
API endpoint for SEO brief generation
"""

import logging
from fastapi import APIRouter, HTTPException

from app.schemas.brief import BriefRequest, BriefResponse
from app.services.gemini import gemini_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/generate-brief", response_model=BriefResponse)
async def generate_brief(request: BriefRequest) -> BriefResponse:
    """
    Generate an SEO content brief using AI
    
    Takes content parameters and returns a comprehensive SEO brief
    as plain text that can be easily copied and used.
    """
    try:
        # Generate the brief using Gemini
        brief_text = await gemini_service.generate_brief(
            title=request.title,
            target_audience=request.target_audience,
            primary_keywords=request.primary_keywords,
            secondary_keywords=request.secondary_keywords
        )
        
        return BriefResponse(
            success=True,
            brief=brief_text,
            error=None
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return BriefResponse(
            success=False,
            brief=None,
            error=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error generating brief: {e}")
        return BriefResponse(
            success=False,
            brief=None,
            error=f"Failed to generate SEO brief: {str(e)}"
        )
