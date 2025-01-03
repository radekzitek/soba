"""User model definition and related types."""
from sqlalchemy import Column, Integer, String
from .base import TimestampModel

class User(TimestampModel):
    """
    User model representing system users.
    
    Attributes:
        user_login: Unique username for login
        user_pass: Hashed password
        user_full_name: User's full name
        user_email: Unique email address
        user_note: Optional notes about the user
    """
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    user_login = Column(String(255), unique=True, nullable=False)
    user_pass = Column(String(255), nullable=False)
    user_full_name = Column(String(255), nullable=False)
    user_email = Column(String(255), unique=True, nullable=False)
    user_note = Column(String(255), nullable=True)