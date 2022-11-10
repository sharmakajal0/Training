from fastapi import APIRouter

from apis.v1 import route_users, route_blogs, route_login

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_blogs.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])