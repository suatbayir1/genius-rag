from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.exceptions.base import AppException
from app.exceptions.exception_handlers import app_exception_handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.add_exception_handler(AppException, app_exception_handler)


@app.get("/")
async def root():
    """Server health check endpoint."""
    return {"message": "Server is running on port 8000"}
