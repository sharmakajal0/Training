import math, random

from typing import NoReturn, Union

from fastapi import Depends, HTTPException
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import table, column
from datetime import datetime, timedelta

from app.v1.user.exception import (
    DuplicateEmailOrNicknameException,
    UserNotFoundException,
    OtpMismatchException,
    PasswordNotChangedException
)
from app.v1.user.models import UserModel
from app.v1.user.repository import UserRepo
from app.v1.user.schema import (
    User, 
    CreateUserRequest,
    UserUpdateRequest,
    CreateUserResponse,
)
from core.utils.token_helper import TokenHelper
from app.v1.user.service import email as _email

token_helper = TokenHelper()

class UserCommandService:
    def __init__(self, user_repo: UserRepo = Depends(UserRepo)):
        self.user_repo = user_repo

    async def create_user(
        self, user: CreateUserRequest
    ) -> Union[CreateUserResponse, NoReturn]:
        if await self.user_repo.get_by_email(
            email=user.email,
        ):
            raise DuplicateEmailOrNicknameException

        # await _email.send_verification(email=user.email, username=user.username)
        
        new_user = UserModel.create(
            name=user.name,
            username=user.username,
            email=user.email,
            password=user.password
        )

        new_user = await self.user_repo.save(new_user=new_user)
        await self.user_repo.session.commit()
        await self.user_repo.session.refresh(new_user)
        return new_user

    async def update_user(
        self, id: int, user: UserUpdateRequest
    ) -> Union[User, NoReturn]:
        get_user = await self.user_repo.get_by_id(user_id=id)
        if not get_user:
            raise UserNotFoundException
        
        if len(user.name.strip()) != 0:
            get_user.name = user.name
        if len(user.username.strip()) != 0:
            get_user.username = user.username
        if len(user.email.strip()) != 0:
            get_user.email = user.email
        
        await self.user_repo.save(new_user=get_user)
        return get_user

    async def delete_user(
        self, id: int
    ) -> None:
        get_user = await self.user_repo.get_by_id(id)
        if not get_user:
            raise UserNotFoundException
        
        return await self.user_repo.delete(get_user)

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

    async def send_otp(self, email: str):
        user = await self.user_repo.get_by_email(email=email)
        if user is None:
            raise UserNotFoundException
        
        digits = [i for i in range(0, 10)]

        otp = ""
        for i in range(6):
            index = math.floor(random.random() * 10)
            otp += str(digits[index])

        expire = 5

        token_helper.access_token = token_helper.encode(username=user.username, expire_period=expire)
        await self.update_otp(user.id, otp)
        # await _email.send_email(email=user.email, otp=otp)
        return {"otp": otp}
        # await self.update_otp(user.id, otp)
        # return {"status": "password sent successfully"}
    
    async def update_otp(self, user_id: int, otp: str):
        current_user = await self.user_repo.get_by_id(user_id=user_id)
        current_user.otp = otp
        await self.user_repo.session.commit()
        

    async def reset_password(self, otp: str, password1: str, password2: str):
        token = token_helper.access_token
        username = await self.user_repo.get_user_by_token(token)
        user = await self.user_repo.get_by_username(username)
        if user.otp != otp:
            raise OtpMismatchException
        if not user.change_password(password1, password2):
            raise PasswordNotChangedException
        await self.user_repo.session.commit()
        await self.update_otp(user.id, "")
        return {"status": "password updated successfully"}
        
