from typing import List, Optional

from fastapi import Depends
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.v1.user.models import UserModel
from app.v1.user.schema import GetUserResponse, User
from core.db import session
from core.utils.token_helper import TokenHelper

token_helper = TokenHelper()

class UserRepo:
    def __init__(self, db: AsyncSession = Depends(session)):
        self.session = db

    async def get_by_id(self, user_id: int) -> Optional[UserModel]:
        user = await self.session.get(UserModel, user_id)
        return user

    async def get_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        query = await self.session.execute(
            select(UserModel).where(
                or_(UserModel.email == email)
            )
        )

        return query.scalars().first()

    async def get_by_username(self, username: str) -> Optional[UserModel]:
        query = await self.session.execute(
            select(UserModel).where(
                or_(UserModel.username == username)
            )
        )

        return query.scalars().first()

    async def get_users(self) -> List[User]:
        query = await self.session.execute(select(UserModel))
        return query.scalars().all()

    async def save(self, new_user: UserModel) -> UserModel:
        self.session.add(new_user)
        return new_user

    async def delete(self, user: UserModel) -> bool:
        await self.session.delete(user)
        await self.session.commit()
    
    async def get_user_by_token(self, token: str):
        username = token_helper.decode(token=token)
        return username
