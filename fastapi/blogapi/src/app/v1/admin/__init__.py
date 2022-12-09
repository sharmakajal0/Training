from fastapi import APIRouter

from .controller.admin_controller import router as admin_router

router = APIRouter()
router.include_router(admin_router, prefix="/admin", tags=["Admin"])

__all__ = ["router"]