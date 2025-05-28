from authx import AuthX, AuthXConfig
from os import getenv
from dotenv import load_dotenv

load_dotenv()

config = AuthXConfig(JWT_ALGORITHM="HS256", JWT_SECRET_KEY=getenv("JWT_SECRET_KEY"))


authx = AuthX(config=config)

def create_jwt_token(username: str):
    token = authx.create_access_token(uid=username)
    return token