"""
SQLAlchemy models for user management.
Defines the database structure for the user table.
"""
from sqlalchemy import Column, Integer, String, DateTime, sql
from ..database import Base

class User(Base):
    """
    User model representing the user_table in the database.
    
    Attributes:
        id (int): Primary key
        created_at (datetime): Timestamp of user creation
        user_login (str): Unique username for login
        user_pass (str): Hashed password
        user_full_name (str): User's full name
        user_email (str): Unique email address
        user_note (str): Optional notes about the user
    """
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    user_login = Column(String(255), unique=True, nullable=False)
    user_pass = Column(String(255), nullable=False)
    user_full_name = Column(String(255), nullable=False)
    user_email = Column(String(255), unique=True, nullable=False)
    user_note = Column(String(255), nullable=True)