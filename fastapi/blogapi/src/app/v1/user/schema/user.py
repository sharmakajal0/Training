from datetime import datetime

from fastapi_utils.api_model import APIModel
from pydantic import Field


class User(APIModel):
    id: int = Field(None, description="ID")
    name: str = Field(None, description="Name")
    username: str = Field(None, description="Username")
    password: str = Field(None, description="Password")
    email: str = Field(None, description="Email")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")
    otp: str = Field(None, description="OTP")
