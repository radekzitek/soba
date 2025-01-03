"""Account model definition and related types."""
from sqlalchemy import Column, Integer, String, Numeric, Boolean, Enum
from .base import TimestampModel
import enum

class AccountType(str, enum.Enum):
    """Valid account types."""
    cash = "cash"
    checking = "checking"
    savings = "savings"
    credit_card = "credit_card"
    investment = "investment"

class Account(TimestampModel):
    """
    Account model representing financial accounts.
    
    Attributes:
        name: Account name
        account_type: Type of account (cash, checking, etc.)
        initial_balance: Starting balance when account was created
        current_balance: Current account balance
        currency: Three-letter currency code (e.g., USD)
        is_active: Whether the account is active
        description: Optional account description
    """
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    account_type = Column(
        Enum(AccountType, name='account_type', create_type=False),
        nullable=False
    )
    initial_balance = Column(Numeric(12, 2), nullable=False, default=0)
    current_balance = Column(Numeric(12, 2), nullable=False, default=0)
    currency = Column(String(3), nullable=False, default="USD")
    is_active = Column(Boolean, default=True)
    description = Column(String, nullable=True) 