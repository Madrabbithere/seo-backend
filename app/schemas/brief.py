"""
Pydantic schemas for SEO Brief API
"""

from pydantic import BaseModel, Field


class BriefRequest(BaseModel):
    """Request schema for generating SEO brief"""
    
    title: str = Field(
        ...,
        min_length=5,
        max_length=200,
        description="The title or topic for the SEO content",
        json_schema_extra={"example": "Best Running Shoes for Marathon Training 2024"}
    )
    
    target_audience: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Description of the target audience",
        json_schema_extra={"example": "Marathon runners aged 25-45 looking for performance footwear"}
    )
    
    primary_keywords: list[str] = Field(
        ...,
        min_length=1,
        max_length=5,
        description="Primary keywords to target (1-5)",
        json_schema_extra={"example": ["running shoes", "marathon shoes"]}
    )
    
    secondary_keywords: list[str] = Field(
        default=[],
        max_length=10,
        description="Secondary keywords to include (optional, up to 10)",
        json_schema_extra={"example": ["cushioning", "durability", "lightweight"]}
    )


class SEOBrief(BaseModel):
    """Schema for the generated SEO brief"""
    
    meta_title: str = Field(..., description="Suggested meta title (under 60 chars)")
    meta_description: str = Field(..., description="Suggested meta description (under 155 chars)")
    h1_suggestion: str = Field(..., description="Suggested H1 heading")
    content_outline: list[str] = Field(..., description="Content outline sections")
    word_count_recommendation: int = Field(..., description="Recommended word count")
    keyword_placement_tips: list[str] = Field(..., description="Tips for keyword placement")
    internal_linking_suggestions: list[str] = Field(..., description="Suggested internal links")


class BriefResponse(BaseModel):
    """Response schema for the brief generation endpoint"""
    
    success: bool = Field(..., description="Whether the request was successful")
    brief: SEOBrief | None = Field(None, description="The generated SEO brief")
    error: str | None = Field(None, description="Error message if request failed")
