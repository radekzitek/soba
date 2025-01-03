"""CRUD operations for users."""
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .base import CRUDBase
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..core.security import get_password_hash, verify_password

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """CRUD operations for users."""
    
    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[User]:
        """Get a user by email address."""
        result = await db.execute(select(User).filter(User.user_email == email))
        return result.scalar_one_or_none()
    
    async def get_by_login(self, db: AsyncSession, *, login: str) -> Optional[User]:
        """Get a user by login name."""
        result = await db.execute(select(User).filter(User.user_login == login))
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> User:
        """Create a new user with password hashing."""
        db_obj = User(
            user_login=obj_in.user_login,
            user_pass=get_password_hash(obj_in.user_pass),
            user_full_name=obj_in.user_full_name,
            user_email=obj_in.user_email,
            user_note=obj_in.user_note
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def authenticate(self, db: AsyncSession, *, login: str, password: str) -> Optional[User]:
        """Authenticate a user by login and password."""
        user = await self.get_by_login(db, login=login)
        if not user:
            return None
        if not verify_password(password, user.user_pass):
            return None
        return user

    async def change_password(
        self,
        db: AsyncSession,
        *,
        user_obj: User,
        current_password: str,
        new_password: str
    ) -> bool:
        """Change user's password."""
        if not verify_password(current_password, user_obj.user_pass):
            return False
        user_obj.user_pass = get_password_hash(new_password)
        await db.commit()
        return True

user = CRUDUser(User) 