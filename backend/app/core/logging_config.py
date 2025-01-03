"""Logging configuration for the application."""
import logging
import logging.handlers
from pathlib import Path
from .config import get_settings

settings = get_settings()

# Log file setup
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
MAX_BYTES = 1024 * 1024  # 1MB
BACKUP_COUNT = 5

def setup_logging() -> None:
    """
    Configure application logging.
    
    Sets up:
    - File logging with rotation
    - Custom formatting
    - Different log levels based on environment
    """
    # Ensure log directory exists
    LOG_DIR.mkdir(exist_ok=True)
    
    # Create formatter
    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)
    
    # Configure file handler
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    
    # Set specific log levels
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    
    # Log startup information
    root_logger.info(
        "Starting application | Version: %s | Environment: %s",
        settings.VERSION,
        settings.ENVIRONMENT
    ) 