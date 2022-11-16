from datetime import datetime

from .request import CreateBlogRequest, CreateGetBlogRequest

class CreateBlogResponse(CreateBlogRequest):
    title: str
    tag: str
    content: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "My First Blog",
                "tag": "Tourism",
                "title": "Into the Himalayas"
            }
        }

class GetBlogResponse(CreateGetBlogRequest):
    title: str
    tag: str
    content: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "My First Blog",
                "tag": "Tourism",
                "title": "Into the Himalayas"
            }
        }