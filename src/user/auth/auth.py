from authx import AuthX, AuthXConfig, RequestToken
from os import getenv
from dotenv import load_dotenv

load_dotenv()

config = AuthXConfig(JWT_ALGORITHM="HS256", JWT_SECRET_KEY=getenv("JWT_SECRET_KEY"), JWT_ACCESS_COOKIE_NAME="access_token")


authx = AuthX(config=config)

def create_jwt_token(username: str) -> str:
    token = authx.create_access_token(uid=username)
    return token

def decode_jwt_token(token: RequestToken) -> str:
    verify = authx.verify_token(token, verify_csrf=False, verify_fresh=False, verify_type=True)
    return verify.sub

