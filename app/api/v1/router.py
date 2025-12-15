"""
API v1 Router
"""

from fastapi import APIRouter

from app.api.v1.endpoints import brief

api_router = APIRouter()

# Include brief router
api_router.include_router(
    brief.router,
    tags=["SEO Brief"]
)
