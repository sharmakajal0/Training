from typing import Union, List, NoReturn
from fastapi import Depends, APIRouter
from fastapi_utils.inferring_router import InferringRouter

from app.v1.user.schema import (
    CreateUserResponse,
    UserUpdateRequest,
    CreateUserRequest, 
    User,
    GetUserResponse
)
from app.v1.user.models import UserModel
from app.v1.user.service.user_command import UserCommandService
from app.v1.user.exception import UserNotFoundException
from core.fastapi_utils.schemas.response import ExceptionResponseSchema

router = APIRouter()

class AdminController:
    @router.post(
        "/", 
        response_model=CreateUserResponse,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="create user")
    async def create_user(
        request: CreateUserRequest,
        service: UserCommandService = Depends(UserCommandService)
    ) -> Union[User, NoReturn]:
        user = await service.create_user(request)
        return user

    @router.get(
        "/",
        response_model=List[User],
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Get Users"
    )
    async def get_all_users(
        service: UserCommandService = Depends(UserCommandService)
    ) -> Union[List[User], None]:
        users = await service.user_repo.get_users()
        return users

    @router.get(
        "/{id}",
        response_model=User,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Get User"
    )
    async def get_user(
        id: int,
        service: UserCommandService = Depends(UserCommandService)
    ) -> Union[User, None]:
        user = await service.user_repo.get_by_id(user_id=id)
        if not user:
            raise UserNotFoundException
        return user

    @router.put(
        "/{id}",
        response_model=User,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Update User"
    )
    async def update_user(
        id: int,
        request: UserUpdateRequest,
        service: UserCommandService = Depends(UserCommandService)
    ) -> Union[User, None]:
        updated_user = await service.update_user(id=id, user=request)
        return updated_user

    @router.delete(
        "/{id}",
        responses={"400": {"model": ExceptionResponseSchema}}
        )
    async def delete_user(id: int, service: UserCommandService = Depends(UserCommandService)):
        await service.delete_user(id)