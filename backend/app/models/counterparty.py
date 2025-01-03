"""Counterparty model definition."""
from sqlalchemy import Column, Integer, String, Boolean, Text
from .base import TimestampModel

class Counterparty(TimestampModel):
    """
    Counterparty model representing transaction participants.
    
    Attributes:
        name: Name of the counterparty (unique)
        description: Optional description
        is_active: Whether the counterparty is active
    """
    __tablename__ = "counterparties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True) 