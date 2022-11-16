from typing import NoReturn, Optional, Union

from sqlalchemy import BigInteger, Column, Unicode

from app.v1.user.exception import PasswordDoesNotMatchException
from app.v1.user.schema import User
from core.db import Base
from core.db.mixins import TimestampMixin


class UserModel(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    password = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    nickname = Column(Unicode(255), nullable=False, unique=True)

    def __init__(self, password: str, email: str, nickname: str):
        self.password = password
        self.email = email
        self.nickname = nickname

    @classmethod
    def _is_password_match(cls, password1: str, password2: str) -> bool:
        return password1 == password2

    @classmethod
    def create(
        cls,
        password1: str,
        password2: str,
        email: str,
        nickname: str,
        is_admin: bool = False,
    ) -> Union["User", NoReturn]:
        if not cls._is_password_match(password1=password1, password2=password2):
            raise PasswordDoesNotMatchException

        return cls(password=password1, email=email, nickname=nickname)

    def change_password(self, password1: str, password2: str) -> Optional[NoReturn]:
        if not self._is_password_match(password1=password1, password2=password2):
            raise PasswordDoesNotMatchException

        self.password = password1
