"""
Logging configuration for the application
"""
import logging
import logging.handlers
from pathlib import Path

# Log file setup
LOG_FILE = Path("logs/app.log")
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
MAX_BYTES = 1024 * 1024  # 1MB
BACKUP_COUNT = 5

def setup_logging():
    """Configure application logging"""
    # Ensure log directory exists
    LOG_FILE.parent.mkdir(exist_ok=True)
    
    # Create formatter
    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Configure file handler
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    
    # Set specific log levels
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING) 