from typing import Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class BlogCreate(BlogBase):
    title : str
    content : str

class ShowBlog(BlogBase):
    title : str
    content : str

    class Config():
        orm_mode = True