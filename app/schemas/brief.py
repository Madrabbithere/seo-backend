"""
Pydantic schemas for SEO Brief API
"""

from pydantic import BaseModel, Field


class BriefRequest(BaseModel):
    """Request schema for generating an SEO brief"""
    
    title: str = Field(
        ...,
        min_length=5,
        max_length=200,
        description="The content title or topic",
        json_schema_extra={"example": "Best Running Shoes for Marathon Training 2024"}
    )
    target_audience: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Description of the target audience",
        json_schema_extra={"example": "Marathon runners aged 25-45 looking for high-performance footwear"}
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
        description="Secondary keywords (optional, up to 10)",
        json_schema_extra={"example": ["cushioning", "durability"]}
    )


class BriefResponse(BaseModel):
    """Response schema containing the generated SEO brief"""
    
    success: bool = Field(
        ...,
        description="Whether the brief was generated successfully"
    )
    brief: str | None = Field(
        default=None,
        description="The generated SEO brief as plain text"
    )
    error: str | None = Field(
        default=None,
        description="Error message if generation failed"
    )
