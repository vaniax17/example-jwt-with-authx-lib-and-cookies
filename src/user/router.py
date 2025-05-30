from authx import RequestToken
from fastapi import APIRouter, HTTPException, Response, Depends, Request, status
from src.database.workwithdb import check_user_in_db, check_correctly_password, create_user
from src.user.auth.auth import create_jwt_token, decode_jwt_token

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/create_user")
async def create_user_endpoint(username: str, password: str, email: str):
    await create_user(username, password, email)
    return {"success": True, "message": "create User success"}
@router.get("/login")
async def login_to_app_endpoint(username: str, password: str, response: Response):
    checker = await check_user_in_db(username)
    if checker:
        password_check = await check_correctly_password(username, password)
        if password_check:
            token = create_jwt_token(username=username)
            response.set_cookie(key="access_token", value=token, httponly=True)
            return {"success": True, "access_token": token, "message": "login success"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

async def get_token_from_cookie(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token missing from cookies"
        )
    return token

@router.get("/protected")
async def protected_endpoint(token: str = Depends(get_token_from_cookie)):
    return {"username": decode_jwt_token(token)}
