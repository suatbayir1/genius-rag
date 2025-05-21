import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import router
from app.config import settings
from app.exceptions.base import AppException
from app.exceptions.exception_handlers import app_exception_handler

app = FastAPI()

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=settings.UPLOAD_DIR), name="static")

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
