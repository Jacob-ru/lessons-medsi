from fastapi import APIRouter

from .v1.routes import router as router_v1

router = APIRouter()

router.include_router(router_v1)
