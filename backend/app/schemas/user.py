from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    user_login: str
    user_full_name: str
    user_email: EmailStr
    user_note: Optional[str] = None

class UserCreate(UserBase):
    user_pass: str

class UserUpdate(BaseModel):
    user_full_name: Optional[str] = None
    user_email: Optional[EmailStr] = None
    user_note: Optional[str] = None

class PasswordChange(BaseModel):
    current_password: str
    new_password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str