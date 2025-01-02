from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..core.security import get_password_hash, verify_password

async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    query = select(User).where(User.user_email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_user_by_login(db: AsyncSession, login: str) -> Optional[User]:
    query = select(User).where(User.user_login == login)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
    query = select(User).offset(skip).limit(limit)
    result = await db.execute(query)
    return list(result.scalars().all())

async def create_user(db: AsyncSession, user: UserCreate) -> User:
    db_user = User(
        user_login=user.user_login,
        user_pass=get_password_hash(user.user_pass),
        user_full_name=user.user_full_name,
        user_email=user.user_email,
        user_note=user.user_note
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def authenticate_user(db: AsyncSession, login: str, password: str) -> Optional[User]:
    user = await get_user_by_login(db, login)
    if not user or not verify_password(password, user.user_pass):
        return None
    return user

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate) -> Optional[User]:
    db_user = await get_user(db, user_id)
    if not db_user:
        return None

    user_data = user_update.model_dump(exclude_unset=True)
    for field, value in user_data.items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)
    return db_user

async def change_password(
    db: AsyncSession, 
    user_id: int, 
    current_password: str, 
    new_password: str
) -> bool:
    db_user = await get_user(db, user_id)
    if not db_user or not verify_password(current_password, db_user.user_pass):
        return False
    
    db_user.user_pass = get_password_hash(new_password)
    await db.commit()
    return True 