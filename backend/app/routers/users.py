"""User management endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from datetime import timedelta

from ..database import get_db
from ..crud.users import user
from ..schemas.user import User, UserCreate, UserUpdate, Token, PasswordChange
from ..core.security import create_access_token
from ..core.deps import get_current_user
from ..core.config import get_settings

settings = get_settings()
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/token", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """
    OAuth2 compatible token login.
    
    Returns an access token if authentication is successful.
    """
    authenticated_user = await user.authenticate(
        db, login=form_data.username, password=form_data.password
    )
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(authenticated_user.id)},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=User)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Create new user.
    
    Checks for email uniqueness before creation.
    """
    db_user = await user.get_by_email(db, email=user_in.user_email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await user.create(db, obj_in=user_in)

@router.get("/me", response_model=User)
async def read_current_user(
    current_user: User = Depends(get_current_user)
):
    """Get current authenticated user."""
    return current_user

@router.put("/me", response_model=User)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update current user's information."""
    return await user.update(db, db_obj=current_user, obj_in=user_update)

@router.post("/me/password", response_model=dict)
async def change_current_user_password(
    password_data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Change current user's password."""
    if await user.change_password(
        db,
        user_obj=current_user,
        current_password=password_data.current_password,
        new_password=password_data.new_password
    ):
        return {"message": "Password updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid current password"
    )

# ... other user endpoints 