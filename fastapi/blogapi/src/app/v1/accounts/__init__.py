from fastapi import APIRouter
from .controller.account_controller import router as account_router

router = APIRouter()
router.include_router(account_router, prefix="/account", tags=["Account"])

__all__ = [
    "router"
]