from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from ..database import get_db
from ..core.deps import get_current_user
from ..schemas import debug as schemas
from ..schemas.user import User
import platform
import fastapi
import sqlalchemy
import pydantic

router = APIRouter(tags=["system"])

@router.get("/health", response_model=dict)
async def health_check(db: AsyncSession = Depends(get_db)):
    """Health check endpoint"""
    try:
        await db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail="Service unhealthy - database connection failed"
        )

@router.get("/debug/system", response_model=schemas.SystemInfo)
async def get_system_info(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get system debug information"""
    from ..core.config import get_settings
    from ..core.logging_config import LOG_FILE, LOG_FORMAT, MAX_BYTES, BACKUP_COUNT
    
    settings = get_settings()
    
    return {
        "versions": {
            "backend_version": "0.1.2",
            "python_version": platform.python_version(),
            "fastapi_version": fastapi.__version__,
            "sqlalchemy_version": sqlalchemy.__version__,
            "pydantic_version": pydantic.__version__
        },
        "environment": settings.ENVIRONMENT,
        "database": {
            "connected": "true",
            "database_name": settings.DATABASE_NAME,
            "host": settings.DATABASE_HOST,
            "port": settings.DATABASE_PORT,
            "user": settings.DATABASE_USER
        },
        "logging_config": {
            "log_level": "INFO",
            "log_file": str(LOG_FILE),
            "log_format": str(LOG_FORMAT),
            "max_file_size": str(MAX_BYTES),
            "backup_count": str(BACKUP_COUNT)
        },
        "cors_origins": ["*"]
    } 