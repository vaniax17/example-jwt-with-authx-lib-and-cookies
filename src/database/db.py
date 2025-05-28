from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(URL, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

@asynccontextmanager
async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()