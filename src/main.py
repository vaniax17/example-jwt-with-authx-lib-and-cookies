from authx import RequestToken
from fastapi import FastAPI, HTTPException, Response, Depends
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from src.database.workwithdb import check_user_in_db, check_correctly_password, create_user, create_db_and_tables
from asyncio import run as asyncio_run
from src.user.router import router as user_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
    asyncio_run(create_db_and_tables())