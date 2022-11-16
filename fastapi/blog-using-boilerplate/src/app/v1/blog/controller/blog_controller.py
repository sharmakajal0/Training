from typing import NoReturn, Union

from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from ..schema import CreateBlogRequest, CreateBlogResponse, Blog
from ..service import BlogCommandService
from core.fastapi.schemas.response import ExceptionResponseSchema

router = InferringRouter()

@cbv(router=router)
class BlogController:
    @router.post(
        "/", 
        response_model=CreateBlogResponse,
        responses={"400": {"model": ExceptionResponseSchema}},
        summary="Create Blog"
    )
    async def create_blog(
        self,
        request: CreateBlogRequest,
        service: BlogCommandService = Depends(BlogCommandService),
    ) -> Union[Blog, NoReturn]:
        return await service.create_blog(**request.dict())