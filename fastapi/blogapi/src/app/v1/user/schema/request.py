from typing import Union
from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "hide",
                "username": "hide",
                "email": "hide@hide.com",
                "password": "pw"
            }
        }

class UserUpdateRequest(BaseModel):
    name: Union[str, None]
    username: Union[str, None]
    email: Union[EmailStr, None]

    class Config:
        schema_extra = {
            "example": {
                "name": "naruto uzumaki",
                "username": "strongestninja",
                "email": "naruto@gmail.com"
            }
        }

class UpdatePasswordRequest(BaseModel):
    password1: str
    password2: str

    class Config:
        schema_extra = {
            "example": {
                "password1": "pw",
                "password2": "pw",
            }
        }