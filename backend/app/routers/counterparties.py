"""Counterparty management endpoints."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from ..crud.counterparties import counterparty
from ..schemas.counterparty import Counterparty, CounterpartyCreate, CounterpartyUpdate
from ..core.deps import get_current_user

router = APIRouter(
    prefix="/counterparties",
    tags=["counterparties"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/", response_model=List[Counterparty])
async def read_counterparties(
    skip: int = 0,
    limit: int = 100,
    include_inactive: bool = False,
    db: AsyncSession = Depends(get_db)
):
    """Get list of counterparties."""
    if include_inactive:
        return await counterparty.get_multi(db, skip=skip, limit=limit)
    return await counterparty.get_active(db, skip=skip, limit=limit)

@router.post("/", response_model=Counterparty)
async def create_counterparty(
    counterparty_in: CounterpartyCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create new counterparty."""
    db_counterparty = await counterparty.get_by_name(db, name=counterparty_in.name)
    if db_counterparty:
        raise HTTPException(status_code=400, detail="Name already registered")
    return await counterparty.create(db, obj_in=counterparty_in)

@router.get("/{counterparty_id}", response_model=Counterparty)
async def read_counterparty(
    counterparty_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific counterparty by ID."""
    db_counterparty = await counterparty.get(db, counterparty_id)
    if db_counterparty is None:
        raise HTTPException(status_code=404, detail="Counterparty not found")
    return db_counterparty

@router.put("/{counterparty_id}", response_model=Counterparty)
async def update_counterparty(
    counterparty_id: int,
    counterparty_update: CounterpartyUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a counterparty."""
    db_counterparty = await counterparty.get(db, counterparty_id)
    if db_counterparty is None:
        raise HTTPException(status_code=404, detail="Counterparty not found")
    return await counterparty.update(db, db_obj=db_counterparty, obj_in=counterparty_update)

@router.delete("/{counterparty_id}")
async def delete_counterparty(
    counterparty_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a counterparty."""
    if not await counterparty.delete(db, id=counterparty_id):
        raise HTTPException(status_code=404, detail="Counterparty not found")
    return {"ok": True} 