"""CRUD operations for counterparties."""
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .base import CRUDBase
from ..models.counterparty import Counterparty
from ..schemas.counterparty import CounterpartyCreate, CounterpartyUpdate

class CRUDCounterparty(CRUDBase[Counterparty, CounterpartyCreate, CounterpartyUpdate]):
    """CRUD operations for counterparties."""
    
    async def get_by_name(self, db: AsyncSession, *, name: str):
        """Get a counterparty by name."""
        result = await db.execute(
            select(Counterparty).filter(Counterparty.name == name)
        )
        return result.scalar_one_or_none()

    async def get_active(
        self,
        db: AsyncSession,
        *,
        skip: int = 0,
        limit: int = 100
    ) -> List[Counterparty]:
        """Get list of active counterparties."""
        result = await db.execute(
            select(Counterparty)
            .filter(Counterparty.is_active == True)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

counterparty = CRUDCounterparty(Counterparty) 