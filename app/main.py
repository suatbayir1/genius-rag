from fastapi import FastAPI

from app.api import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    """Server health check endpoint."""
    return {"message": "Server is running on port 8000"}
