from fastapi import APIRouter

from .controller.user_controller import UserController, router as user_router
from .repository import UserRepo
from .repository.user_repo import UserRepo

router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["User"])

__all__ = ["router"]
