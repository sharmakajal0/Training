from typing import List, Optional

from fastapi import Depends
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.v1.user.models import UserModel
from core.db.session import db_session


class UserRepo:
    def __init__(self, db: AsyncSession = Depends(db_session)):
        self.session = db

    async def get_by_id(self, user_id: int) -> Optional[UserModel]:
        return await self.session.get(UserModel, user_id)

    async def get_by_email_or_nickname(
        self,
        email: str,
        nickname: str,
    ) -> Optional[UserModel]:
        query = await self.session.execute(
            select(UserModel).where(
                or_(UserModel.email == email, UserModel.nickname == nickname)
            )
        )

        return query.scalars().first()

    async def get_users(self) -> List[UserModel]:
        query = await self.session.execute(select(UserModel))
        return query.scalars().all()

    async def save(self, user: UserModel) -> UserModel:
        self.session.add(user)
        return user

    async def delete(self, user: UserModel) -> None:
        await self.session.delete(user)
