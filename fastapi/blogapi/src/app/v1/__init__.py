from fastapi import APIRouter

from .user import router as user_router
from .admin import router as admin_router
from .accounts import router as account_router

router = APIRouter()
router.include_router(admin_router)
router.include_router(account_router)
router.include_router(user_router)


__all__ = ["router"]
