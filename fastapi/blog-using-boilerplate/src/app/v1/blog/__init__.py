from fastapi import APIRouter

from .controller.blog_controller import router as blog_router

router = APIRouter()
router.include_router(blog_router, prefix="/blog", tags=["Blog"])

__all__ = ["router"]