from fastapi import FastAPI, HTTPException, Depends
from uvicorn import run
from src.database.workwithdb import check_user_in_db, check_correctly_password, create_user, create_db_and_tables
from auth.auth import create_jwt_token
app = FastAPI()


@app.post("/create_user")
async def create_user_endpoint(username: str, password: str, email: str):
    await create_user(username, password, email)
    return {"success": True, "message": "create User success"}
@app.get("/login")
async def login_to_app_endpoint(username: str, password: str):
    checker = await check_user_in_db(username)
    if checker:
        password_check = await check_correctly_password(username, password)
        if password_check:
            token = create_jwt_token(username=username)
            return {"success": True, "access_token": token, "message": "login success"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)