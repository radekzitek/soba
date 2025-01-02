from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from ..database import get_db
from .. import crud
from .security import verify_token
from ..models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """
    Validates JWT token and returns the current user.
    Raises 401 if token is invalid or user not found.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify token and extract user_id
    user_id = verify_token(token)
    if user_id is None:
        raise credentials_exception
        
    # Get user from database using ID
    user = await crud.get_user(db, int(user_id))
    if user is None:
        raise credentials_exception
        
    return user 