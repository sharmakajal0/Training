from fastapi_utils.api_model import APIModel
from pydantic import Field

class Blog(APIModel):
    id: int = Field(None, description="ID")
    title: str = Field(None, description="Title")
    tag: str = Field(None, description="Tag")
    content: str = Field(None, description="content")