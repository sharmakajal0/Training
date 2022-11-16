from typing import NoReturn, Union

from fastapi import Depends

from ..models import BlogModel
from ..repository import BlogRepo
from ..schema import Blog

class BlogCommandService:
    def __init__(self, blog_repo: BlogRepo = Depends(BlogRepo)):
        self.blog_repo = blog_repo

    async def create_blog(
        self,
        title: str,
        tag: str,
        content: str
    ) -> Union[Blog, NoReturn]:
        blog = BlogModel.create(title=title,tag=tag,content=content)
        blog = Blog.from_orm(blog)
        await self.blog_repo.save(blog=blog)
        await self.blog_repo.db.commit()
        return blog