from typing import NoReturn, Union

from fastapi import Depends

from app.v1.user.exception import (
    DuplicateEmailOrNicknameException,
    UserNotFoundException,
)
from app.v1.user.models import UserModel
from app.v1.user.repository import UserRepo
from app.v1.user.schema import User


class UserCommandService:
    def __init__(self, user_repo: UserRepo = Depends(UserRepo)):
        self.user_repo = user_repo

    async def create_user(
        self, email: str, password1: str, password2: str, nickname: str
    ) -> Union[User, NoReturn]:
        if await self.user_repo.get_by_email_or_nickname(
            email=email,
            nickname=nickname,
        ):
            raise DuplicateEmailOrNicknameException

        user = UserModel.create(
            password1=password1,
            password2=password2,
            email=email,
            nickname=nickname,
        )
        user = await self.user_repo.save(user=user)
        await self.user_repo.session.commit()
        return User.from_orm(user)

    async def update_password(
        self,
        user_id: int,
        password1: str,
        password2: str,
    ) -> Union[User, NoReturn]:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException

        user.change_password(password1=password1, password2=password2)
        await self.user_repo.session.commit()
        return User.from_orm(user)
