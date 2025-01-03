from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum
from decimal import Decimal

class AccountType(str, Enum):
    cash = "cash"
    checking = "checking"
    savings = "savings"
    credit_card = "credit_card"
    investment = "investment"

class AccountBase(BaseModel):
    name: str
    account_type: AccountType
    initial_balance: Decimal = Field(decimal_places=2, max_digits=12)
    currency: str = "USD"
    is_active: bool = True
    description: Optional[str] = None

class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    account_type: Optional[AccountType] = None
    initial_balance: Optional[Decimal] = Field(None, decimal_places=2, max_digits=12)
    current_balance: Optional[Decimal] = Field(None, decimal_places=2, max_digits=12)
    currency: Optional[str] = None
    is_active: Optional[bool] = None
    description: Optional[str] = None

class Account(AccountBase):
    id: int
    current_balance: Decimal = Field(decimal_places=2, max_digits=12)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 