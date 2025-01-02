from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://soba-db-user:user1234@34.45.245.225/soba-db"

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

AsyncSessionMaker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionMaker() as session:
        yield session 