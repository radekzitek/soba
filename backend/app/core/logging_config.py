"""
Logging configuration for the application.
Sets up a single log file for all application logging.
"""
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

# Configure logging paths and settings
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "app.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO
MAX_BYTES = 1024 * 1024  # 1MB
BACKUP_COUNT = 5

# Define logger names
SQLALCHEMY_LOGGERS = [
    'sqlalchemy.engine',
    'sqlalchemy.pool',
    'sqlalchemy.dialects',
    'sqlalchemy.orm'
]

UVICORN_LOGGERS = [
    'uvicorn',
    'uvicorn.error',
    'uvicorn.access',
    'uvicorn.asgi',
    'uvicorn.protocols'
]

FASTAPI_LOGGERS = [
    'fastapi'
]

def setup_logging() -> None:
    """
    Configures application-wide logging.
    
    - Creates a rotating log file
    - Sets up consistent formatting
    - Ensures all loggers propagate to root
    """
    # Reset existing handlers
    logging.root.handlers = []
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    root_logger.addHandler(file_handler)

    # Ensure all loggers propagate to root
    for logger_name in [*SQLALCHEMY_LOGGERS, *UVICORN_LOGGERS, *FASTAPI_LOGGERS]:
        logger = logging.getLogger(logger_name)
        logger.handlers = []  # Remove any existing handlers
        logger.propagate = True
        logger.setLevel(LOG_LEVEL) 