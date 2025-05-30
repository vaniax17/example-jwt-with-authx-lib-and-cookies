from authx import AuthX, AuthXConfig, RequestToken
from os import getenv

from authx.types import TokenLocation
from dotenv import load_dotenv
from src.user.router import Request

load_dotenv()

config = AuthXConfig(JWT_ALGORITHM="HS256", JWT_SECRET_KEY=getenv("JWT_SECRET_KEY"), JWT_ACCESS_COOKIE_NAME="access_token", JWT_TOKEN_LOCATION=["cookies"])


authx = AuthX(config=config)

def create_jwt_token(username: str) -> str:
    token = authx.create_access_token(uid=username)
    return token

async def decode_jwt_token(request: Request) -> str:
    verify = await authx.get_access_token_from_request(request)
    payload = authx.verify_token(verify, verify_csrf=False)
    return payload.sub