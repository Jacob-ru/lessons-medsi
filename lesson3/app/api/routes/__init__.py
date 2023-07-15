from fastapi import APIRouter

from .v1.routes import router as router_v1
from .v2.routes import router as router_v2

router = APIRouter()

router.include_router(prefix='/v1', router=router_v1)
router.include_router(prefix='/v2', router=router_v2)
