from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from ..database import get_db
from ..crud.user import get_user_by_login
from .security import verify_token
from ..models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    username = verify_token(token)
    if username is None:
        raise credentials_exception
        
    user = await get_user_by_login(db, username)
    if user is None:
        raise credentials_exception
        
    return user 