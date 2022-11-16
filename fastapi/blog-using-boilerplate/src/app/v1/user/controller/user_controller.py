from typing import NoReturn, Union

from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.v1.user.schema import CreateUserRequest, CreateUserResponse, User
from app.v1.user.service.user_command import UserCommandService
from core.fastapi.schemas.response import ExceptionResponseSchema

router = InferringRouter()


@cbv(router=router)
class UserController:
    @router.post(
        "/",
        response_model=CreateUserResponse,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Create User",
    )
    async def create_user(
        self,
        request: CreateUserRequest,
        service: UserCommandService = Depends(UserCommandService),
    ) -> Union[User, NoReturn]:
        return await service.create_user(**request.dict())

    @router.post(
        "/user/{user_id}",
        response_model=CreateUserResponse,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Create User",
    )
    def read_item(
        self, user: str, service: UserCommandService = Depends(UserCommandService)
    ) -> User:
        pass
