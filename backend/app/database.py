"""
Database configuration module.
Handles database connection and session management using SQLAlchemy async engine.
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from .core.config import get_settings

settings = get_settings()

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models"""
    pass

# Create async engine for database connection
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # Disable console echo since we're using file logging
)

# Create session factory for database operations
AsyncSessionMaker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency function that yields database sessions.
    
    Yields:
        AsyncSession: SQLAlchemy async session for database operations
    
    Usage:
        @app.get("/endpoint")
        async def endpoint(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with AsyncSessionMaker() as session:
        yield session 