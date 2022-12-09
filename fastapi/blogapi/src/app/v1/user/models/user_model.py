from typing import NoReturn, Optional, Union
from datetime import datetime

from sqlalchemy import Integer, Column, Unicode, DateTime, Boolean, String
from app.v1.user.exception import PasswordDoesNotMatchException
from app.v1.user.schema import User
from core.db import Base
from core.db.mixins import TimestampMixin


class UserModel(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)
    username = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False)
    password = Column(Unicode(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    otp = Column(String, default=None)

    def __init__(self, name: str, username: str, password: str, email: str):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def _is_password_match(cls, password1: str, password2: str) -> bool:
        return password1 == password2

    @classmethod
    def create(
        cls,
        name: str,
        username: str,
        email: str,
        password: str,
        is_admin: bool = False,
    ) -> Union["User", NoReturn]:
        return cls(name=name, username=username, email=email, password=password)

    def update_otp(self, otp: str):
        self.otp = otp

    def change_password(self, password1: str, password2: str) -> bool:
        is_password_changed = False
        if not self._is_password_match(password1=password1, password2=password2):
            raise PasswordDoesNotMatchException

        self.password = password1
        is_password_changed = True
        return is_password_changed
