"""
SEO Brief generation endpoint
"""

import logging
from fastapi import APIRouter, HTTPException

from app.schemas import BriefRequest, BriefResponse
from app.services import gemini_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/generate-brief",
    response_model=BriefResponse,
    summary="Generate SEO Brief",
    description="Generate a comprehensive SEO content brief using AI"
)
async def generate_brief(request: BriefRequest) -> BriefResponse:
    """
    Generate an SEO brief based on the provided parameters.
    
    - **title**: The content title or topic (5-200 characters)
    - **target_audience**: Description of the target audience (10-500 characters)
    - **primary_keywords**: List of 1-5 primary keywords to target
    - **secondary_keywords**: Optional list of up to 10 secondary keywords
    """
    try:
        logger.info(f"Generating SEO brief for: {request.title}")
        
        brief = await gemini_service.generate_brief(
            title=request.title,
            target_audience=request.target_audience,
            primary_keywords=request.primary_keywords,
            secondary_keywords=request.secondary_keywords
        )
        
        return BriefResponse(
            success=True,
            brief=brief
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return BriefResponse(
            success=False,
            error=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error generating brief: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate SEO brief: {str(e)}"
        )
