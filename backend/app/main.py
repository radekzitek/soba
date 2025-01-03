"""
FastAPI application main module.
Defines API endpoints and application configuration.
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import accounts, users, system, counterparties
from .core.middleware import APILoggingMiddleware
from .core.config import get_settings

# Set up logging
from .core.logging_config import setup_logging
setup_logging()
logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Initialize FastAPI app
app = FastAPI(
    title="Family Finance Manager API",
    version=settings.VERSION,
    description="API for managing family finances"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

# Add logging middleware
app.add_middleware(APILoggingMiddleware)

# Include routers
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(counterparties.router)
app.include_router(system.router)

@app.on_event("startup")
async def init_db():
    """Initialize database on startup."""
    logger.info("Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized successfully") 