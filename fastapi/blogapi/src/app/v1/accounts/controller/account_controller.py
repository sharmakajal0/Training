from fastapi import APIRouter


router = APIRouter()

class AccountController:
    @router.get("/")
    async def get_account():
        pass

    @router.put("/")
    async def update_account():
        pass