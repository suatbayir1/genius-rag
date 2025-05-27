import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.api import router
from app.config import settings
from app.exceptions.base import AppException
from app.exceptions.exception_handlers import app_exception_handler

app = FastAPI()

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://173.249.57.83:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/static/{filename}")
async def serve_static(filename: str, request: Request):
    file_path = os.path.join(settings.UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            headers={
                "Access-Control-Allow-Origin": request.headers.get("origin", "*"),
                "Access-Control-Allow-Credentials": "true",
            },
        )
    return {"error": "File not found"}


app.include_router(router)
app.add_exception_handler(AppException, app_exception_handler)


@app.get("/")
async def root():
    """Server health check endpoint."""
    return {"message": "Server is running on port 8000"}
