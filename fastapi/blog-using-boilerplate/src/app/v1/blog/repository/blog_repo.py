from typing import List, Optional

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.v1.blog.models import BlogModel
from core.db.session import db_session

class BlogRepo:
    def __init__(self, db: AsyncSession = Depends(db_session)):
        self.db = db
    
    async def save(self, blog: BlogModel) -> BlogModel:
        self.db.add(blog)
        return blog