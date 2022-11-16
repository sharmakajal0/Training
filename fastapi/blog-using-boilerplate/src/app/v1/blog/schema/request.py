from pydantic import BaseModel

class CreateBlogRequest(BaseModel):
    title: str
    tag: str
    content: str

    class Config:
        schema_extra = {
            "example": {
                "title": "My First Blog",
                "tag": "Tourism",
                "content": "Into the Himalayas"
            }
        }

class CreateGetBlogRequest:
    title: str

    class Config:
        schema_extra = {
            "example": {
                "title": "My First Blog"
            }
        }