from typing import Any, Coroutine

from authx import AuthX, AuthXConfig, RequestToken
from os import getenv

from authx.types import TokenLocation
from dotenv import load_dotenv
from src.user.router import Request
from src.user.router import Response

load_dotenv()

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY=getenv("JWT_SECRET_KEY"),
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_REFRESH_COOKIE_NAME="refresh_token",
    JWT_TOKEN_LOCATION=["cookies"],
    JWT_COOKIE_CSRF_PROTECT=True,
    JWT_CSRF_IN_COOKIES=True,
    JWT_ACCESS_CSRF_COOKIE_NAME="csrf_access_token",
    JWT_REFRESH_CSRF_COOKIE_NAME="csrf_refresh_token",
)


authx = AuthX(config=config)

def create_jwt_token(username: str, response: Response) -> dict:
    token = authx.create_access_token(uid=username)
    refresh_token = authx.create_refresh_token(uid=username)
    authx.set_access_cookies(token, response)
    authx.set_refresh_cookies(refresh_token, response)
    return {"token": token, "refresh_token": refresh_token}

async def decode_jwt_token(request: Request) -> str:
    verify = await authx.get_access_token_from_request(request)
    payload = authx.verify_token(verify)
    return payload.sub