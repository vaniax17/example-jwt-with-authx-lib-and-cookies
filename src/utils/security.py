import aiobcrypt

async def hash_password(password: str) -> str:
    salt = await aiobcrypt.gensalt()
    hashed = await aiobcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

async def check_password(password: str, hashed_password: str) -> bool:
    return await aiobcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
