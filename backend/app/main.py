"""
FastAPI application main module.
Defines API endpoints and application configuration.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import accounts, users, system
from .core.middleware import APILoggingMiddleware
import logging

# Set up logging
from .core.logging_config import setup_logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Family Finance Manager API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add logging middleware
app.add_middleware(APILoggingMiddleware)

# Include routers
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(system.router)

@app.on_event("startup")
async def init_db():
    logger.info("Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized successfully") 