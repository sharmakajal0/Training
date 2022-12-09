from typing import NoReturn, Union

from fastapi import Depends, APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.v1.user.schema import CreateUserRequest, User, GetUserResponse, CreateUserResponse
from app.v1.user.service.user_command import UserCommandService
from app.v1.user.service.user_query import UserQueryService
from core.fastapi_utils.schemas.response import ExceptionResponseSchema
from app.v1.user.exception import UserNotFoundException

router = APIRouter()

class UserController:
    @router.post(
        "/",
        response_model=CreateUserResponse,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="register User",
    )
    async def create_user(
        request: CreateUserRequest,
        service: UserCommandService = Depends(UserCommandService),
    ) -> Union[User, NoReturn]:
        return await service.create_user(request)

    @router.post(
        "/login",
        summary="login user"
    )
    async def login_user(username: str, password: str, service: UserQueryService = Depends(UserQueryService)):
        access_token = await service.find_user(username=username, password=password)
        return {"access_token": access_token}
        

    @router.post(
        "/logout",
        summary="logout user"
    )
    async def logout_user():
        pass

    @router.post(
        "/forgot",
        summary="forgot password"
    )
    async def forgot_password(email: str, service: UserCommandService = Depends(UserCommandService)):
        return await service.send_otp(email=email)

    @router.post(
        "/reset",
        summary="reset password"
    )
    async def reset_password(otp: str, 
        password1: str, password2: str,
        service: UserCommandService = Depends(UserCommandService)
    ):
        return await service.reset_password(otp, password1, password2)
        
