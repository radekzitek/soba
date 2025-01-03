from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from .. import crud
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
    """Get list of accounts"""
    return await crud.get_accounts(db, skip=skip, limit=limit, include_inactive=include_inactive)

@router.post("/", response_model=Account)
async def create_account(
    account: AccountCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create new account"""
    return await crud.create_account(db=db, account=account)

@router.get("/{account_id}", response_model=Account)
async def read_account(
    account_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get specific account by ID"""
    db_account = await crud.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.put("/{account_id}", response_model=Account)
async def update_account(
    account_id: int,
    account_update: AccountUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update an account"""
    db_account = await crud.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return await crud.update_account(db=db, db_account=db_account, account_update=account_update)

@router.delete("/{account_id}")
async def delete_account(
    account_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete an account"""
    db_account = await crud.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    await crud.delete_account(db=db, db_account=db_account)
    return {"ok": True} 