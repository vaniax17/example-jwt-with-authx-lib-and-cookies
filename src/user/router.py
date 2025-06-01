
from fastapi import APIRouter, HTTPException, Response, Request
from src.database.workwithdb import check_user_and_email_in_db, check_correctly_password, create_user
from src.user.auth.auth import create_jwt_token, decode_jwt_token_in_get_request, logout_of_account

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/create_user")
async def create_user_endpoint(username: str, password: str, email: str):
    return await create_user(username, password, email)

@router.get("/login")
async def login_to_app_endpoint(username: str, password: str, response: Response):
    checker = await check_user_and_email_in_db(username, None)
    if checker:
        password_check = await check_correctly_password(username, password)
        if password_check:
            token = create_jwt_token(username=username, response=response)
            return {"success": True, "access_token": token.get("token"), "refresh_token": token.get("refresh_token"), "message": "login success"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@router.delete("/logout")
def logout_endpoint(response: Response):
    return logout_of_account(response)

@router.get("/protected")
async def protected_endpoint(request: Request):
    try:
        username = await decode_jwt_token_in_get_request(request)
        return {"success": True, "message": "protected endpoint", "username": username}
    except Exception as e:
        return HTTPException(status_code=401, detail=f"Invalid token or {e}")


