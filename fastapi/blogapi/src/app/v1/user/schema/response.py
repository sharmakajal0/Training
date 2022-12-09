from typing import Union
from datetime import datetime

from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: int
    name: str
    usename: str
    email: str
    is_admin: Union[bool, None]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class GetUserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True