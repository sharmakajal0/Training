from typing import List, Optional

from fastapi import Request

class BlogCreationForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.content: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.content = form.get("content")
    
    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.content or not len(self.Content) >= 20:
            self.errors.append("Content too short")
        if not self.errors:
            return True
        return False