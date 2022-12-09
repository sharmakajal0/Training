from fastapi import APIRouter

from .controller.user_controller import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/auth", tags=["Auth"])

__all__ = ["router"]
