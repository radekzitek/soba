"""Counterparty schemas for request/response validation."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CounterpartyBase(BaseModel):
    """Base counterparty attributes."""
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    is_active: bool = True

class CounterpartyCreate(CounterpartyBase):
    """Attributes for creating a counterparty."""
    pass

class CounterpartyUpdate(BaseModel):
    """Attributes for updating a counterparty."""
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    is_active: Optional[bool] = None

class Counterparty(CounterpartyBase):
    """Complete counterparty model with database attributes."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 