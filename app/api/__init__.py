from fastapi import APIRouter

from app.api.repository import repository_router
from app.api.test import test_router

router: APIRouter = APIRouter(prefix="/api/v1", tags=["API"])

router.include_router(repository_router)
router.include_router(test_router)
