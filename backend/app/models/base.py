"""Base model with common fields and functionality."""
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from ..database import Base

class TimestampModel(Base):
    """
    Abstract base model that includes timestamp fields.
    
    Attributes:
        created_at: Timestamp when record was created
        updated_at: Timestamp when record was last updated
    """
    __abstract__ = True
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False) 