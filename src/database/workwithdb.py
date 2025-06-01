from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import select

from src.database.db import Base, get_db, engine
from src.utils import security
from src.user.models.schemas import UserModel

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

async def check_user_and_email_in_db(username: str, email: str) -> bool:
    async with get_db() as db:
        ps_username = await db.execute(select(User).where(User.username == username))
        result_username = ps_username.scalar_one_or_none()
        ps_email = await db.execute(select(User).where(User.email == email))
        result_email = ps_email.scalar_one_or_none()
        if result_username is not None or result_email is not None:
            return True
        else:
            return False

async def create_user(username: str, password: str, email):
    try:
        UserModel(username=username, password=password, email=email)
    except Exception as e:
        return {"success": False, "message": str(e)}

    if await check_user_and_email_in_db(username, email):
        return {"success": False, "message": "User or email already exists"}
    else:
        hashed_password = await security.hash_password(password)
        async with get_db() as db:
            try:
                db.add(User(username=username, hashed_password=hashed_password, email=email))
                await db.commit()
                return {"success": True, "message": "User added"}
            except Exception as e:
                return {"success": False, "message": str(e)}


async def check_correctly_password(username: str, password: str) -> bool:
    async with get_db() as db:
        ps = await db.execute(select(User).where(User.username == username))
        user = ps.scalar_one_or_none()
        check = await security.check_password(password, user.hashed_password)
        if check:
            return True
        else:
            return False