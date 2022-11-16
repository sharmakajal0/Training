from typing import NoReturn, Optional, Union

from sqlalchemy import BigInteger, Integer, ForeignKey, Column, String
from sqlalchemy.orm import relationship

from app.v1.blog.schema import Blog
from app.v1.user.models import UserModel
from core.db import Base
from core.db.mixins import TimestampMixin


class BlogModel(Base, TimestampMixin):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("UserModel")

    def __init__(
        self,
        title: str,
        tag: str,
        content: str
    ):
        self.title = title
        self.tag = tag
        self.content = content

    @classmethod
    def create(
        cls,
        title: str,
        tag: str,
        content: str
    ) -> Union["Blog", NoReturn]:
        # return {"title": title, "tag": tag, "content": content}
        return cls(title=title, tag=tag, content=content)