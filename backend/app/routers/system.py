"""System information and debugging endpoints."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import platform
import fastapi
import sqlalchemy
import pydantic
import logging

from ..database import get_db
from ..core.deps import get_current_user
from ..schemas import debug as schemas
from ..core.config import get_settings
from ..core.logging_config import LOG_FORMAT, MAX_BYTES, BACKUP_COUNT, LOG_FILE

logger = logging.getLogger(__name__)
settings = get_settings()

router = APIRouter(
    prefix="/system",
    tags=["system"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/health", response_model=dict)
async def health_check(db: AsyncSession = Depends(get_db)):
    """Health check endpoint."""
    try:
        await db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        logger.error("Health check failed: %s", str(e))
        raise HTTPException(
            status_code=503,
            detail="Service unavailable"
        )

@router.get("/debug", response_model=schemas.SystemInfo)
async def get_system_info(db: AsyncSession = Depends(get_db)):
    """Get detailed system information for debugging."""
    try:
        await db.execute(text("SELECT 1"))
        db_connected = True
    except Exception:
        db_connected = False
        logger.exception("Database connection check failed")

    return {
        "versions": {
            "backend_version": settings.VERSION,
            "python_version": platform.python_version(),
            "fastapi_version": fastapi.__version__,
            "sqlalchemy_version": sqlalchemy.__version__,
            "pydantic_version": pydantic.__version__
        },
        "environment": settings.ENVIRONMENT,
        "database": {
            "connected": str(db_connected),
            "database_name": settings.DATABASE_NAME,
            "host": settings.DATABASE_HOST,
            "port": settings.DATABASE_PORT,
            "user": settings.DATABASE_USER
        },
        "logging_config": {
            "log_level": settings.LOG_LEVEL,
            "log_file": str(LOG_FILE),
            "log_format": str(LOG_FORMAT),
            "max_file_size": str(MAX_BYTES),
            "backup_count": str(BACKUP_COUNT)
        },
        "cors_origins": settings.CORS_ORIGINS
    } 