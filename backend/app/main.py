from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from datetime import timedelta

from . import crud
from .models import user as models
from .schemas.user import User, UserCreate, UserUpdate, PasswordChange, Token
from .database import engine, get_db, Base
from .core.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(title="User Management API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/token", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_login}, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    db_user = await crud.get_user_by_email(db, user.user_email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = await crud.get_user_by_login(db, user.user_login)
    if db_user:
        raise HTTPException(status_code=400, detail="Login already registered")
    
    return await crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=User)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    db_user = await crud.update_user(db, user_id=user_id, user_update=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/change-password")
async def change_password(
    user_id: int,
    password_change: PasswordChange,
    db: AsyncSession = Depends(get_db)
):
    success = await crud.change_password(
        db,
        user_id=user_id,
        current_password=password_change.current_password,
        new_password=password_change.new_password
    )
    if not success:
        raise HTTPException(status_code=400, detail="Invalid current password")
    return {"message": "Password changed successfully"} 