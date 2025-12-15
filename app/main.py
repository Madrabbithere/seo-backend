"""
SEO Brief Generator API
FastAPI backend for generating SEO briefs using Google Gemini AI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings

# Initialize FastAPI app
app = FastAPI(
    title="SEO Brief Generator API",
    description="Generate comprehensive SEO content briefs using AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "SEO Brief Generator API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for Railway"""
    return {"status": "healthy"}


# Include API router
app.include_router(api_router, prefix="/api/v1")
