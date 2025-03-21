from fastapi import APIRouter

from app.api.repository import repository_router

router: APIRouter = APIRouter(prefix="/api/v1", tags=["API"])

router.include_router(repository_router)
