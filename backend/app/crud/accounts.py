from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from ..models.account import Account
from ..schemas.account import AccountCreate, AccountUpdate

async def get_account(db: AsyncSession, account_id: int) -> Optional[Account]:
    result = await db.execute(select(Account).filter(Account.id == account_id))
    return result.scalar_one_or_none()

async def get_accounts(
    db: AsyncSession, 
    skip: int = 0, 
    limit: int = 100,
    include_inactive: bool = False
) -> List[Account]:
    query = select(Account)
    if not include_inactive:
        query = query.filter(Account.is_active == True)
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def create_account(db: AsyncSession, account: AccountCreate) -> Account:
    db_account = Account(
        name=account.name,
        account_type=account.account_type,
        initial_balance=account.initial_balance,
        current_balance=account.initial_balance,
        currency=account.currency,
        is_active=account.is_active,
        description=account.description
    )
    db.add(db_account)
    await db.commit()
    await db.refresh(db_account)
    return db_account

async def update_account(
    db: AsyncSession,
    db_account: Account,
    account_update: AccountUpdate
) -> Account:
    update_data = account_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_account, field, value)
    
    await db.commit()
    await db.refresh(db_account)
    return db_account

async def delete_account(db: AsyncSession, db_account: Account) -> bool:
    await db.delete(db_account)
    await db.commit()
    return True 