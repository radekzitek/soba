from sqlalchemy import Column, Integer, String, DateTime, sql
from ..database import Base

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    user_login = Column(String(255), unique=True, nullable=False)
    user_pass = Column(String(255), nullable=False)
    user_full_name = Column(String(255), nullable=False)
    user_email = Column(String(255), unique=True, nullable=False)
    user_note = Column(String(255), nullable=True)