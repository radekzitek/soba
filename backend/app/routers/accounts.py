"""Account management endpoints."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from ..crud.accounts import account
from ..schemas.account import Account, AccountCreate, AccountUpdate
from ..schemas.user import User
from ..core.deps import get_current_user

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/", response_model=List[Account])
async def read_accounts(
    skip: int = 0,
    limit: int = 100,
    include_inactive: bool = False,
    db: AsyncSession = Depends(get_db)
):
    """
    Get list of accounts.
    
    Args:
        skip: Number of records to skip (pagination)
        limit: Maximum number of records to return
        include_inactive: Whether to include inactive accounts
        db: Database session
        
    Returns:
        List of accounts
    """
    return await account.get_accounts(
        db,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive
    )

@router.post("/", response_model=Account)
async def create_account(
    account_in: AccountCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create new account."""
    return await account.create(db, obj_in=account_in)

@router.get("/{account_id}", response_model=Account)
async def read_account(
    account_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific account by ID."""
    db_account = await account.get(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.put("/{account_id}", response_model=Account)
async def update_account(
    account_id: int,
    account_update: AccountUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update an account."""
    db_account = await account.get(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return await account.update(db, db_obj=db_account, obj_in=account_update)

@router.delete("/{account_id}")
async def delete_account(
    account_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete an account."""
    if not await account.delete(db, id=account_id):
        raise HTTPException(status_code=404, detail="Account not found")
    return {"ok": True} 