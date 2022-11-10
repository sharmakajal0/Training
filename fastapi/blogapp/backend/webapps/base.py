from webapps.blogs import route_blogs
from webapps.users import route_users
from webapps.auth import route_login
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_blogs.router, prefix="", tags=["blog-webapp"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])