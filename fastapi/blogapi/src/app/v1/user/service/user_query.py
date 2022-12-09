from typing import Optional, Union, NoReturn
from datetime import datetime, timedelta

from fastapi import Depends

from ..exception import UserNotFoundException, PasswordDoesNotMatchException
from ..repository import UserRepo
from ..schema import User
from core.utils.token_helper import TokenHelper

token_helper = TokenHelper()

class UserQueryService:
    def __init__(self, user_repo: UserRepo = Depends(UserRepo)):
        self.user_repo = user_repo

    async def get_user(self, user_id: int) -> Optional[User]:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            raise UserNotFoundException

        return User.from_orm(user)

    async def is_admin(self, user_id: int) -> bool:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            return False

        if user.is_admin is False:
            return False

        return True
    
    async def find_user(self, username: str, password: str) -> str:
        user = None
        if username[-4:] == ".com":
            user = await self.user_repo.get_by_email(username)
            if user is None:
                raise UserNotFoundException
        else:
            user = await self.user_repo.get_by_username(username=username)
            if user is None:
                raise UserNotFoundException
        
        if user.password != password:
            raise PasswordDoesNotMatchException

        expire = 10

        payload = {
            'exp' : datetime.utcnow() + timedelta(days=0, minutes=expire),
            'iat' : datetime.utcnow(),
            'scope': 'access_token',
            'sub': user.username
        }

        access_token = token_helper.encode(payload, expire)
        return access_token

    async def get_user_by_token(self):
        access_token = token_helper.access_token
        print(access_token)
        username = token_helper.decode(access_token)
        user = self.user_repo.get_by_username(username)
        return user

