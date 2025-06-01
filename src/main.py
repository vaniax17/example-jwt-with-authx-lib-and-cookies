from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from src.database.workwithdb import create_db_and_tables
from asyncio import run as asyncio_run
from src.user.router import router as user_router
app = FastAPI()

app.include_router(user_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или "*" для всего
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
    asyncio_run(create_db_and_tables())