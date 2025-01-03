"""CRUD operations for accounts."""
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .base import CRUDBase
from ..models.account import Account
from ..schemas.account import AccountCreate, AccountUpdate

class CRUDAccount(CRUDBase[Account, AccountCreate, AccountUpdate]):
    """CRUD operations for accounts."""
    
    async def get_accounts(
        self,
        db: AsyncSession,
        *,
        skip: int = 0,
        limit: int = 100,
        include_inactive: bool = False
    ) -> List[Account]:
        """
        Get list of accounts with optional inactive filter.
        
        Args:
            db: Database session
            skip: Number of records to skip
            limit: Maximum number of records to return
            include_inactive: Whether to include inactive accounts
            
        Returns:
            List of accounts matching the criteria
        """
        query = select(Account)
        if not include_inactive:
            query = query.filter(Account.is_active == True)
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

account = CRUDAccount(Account) 