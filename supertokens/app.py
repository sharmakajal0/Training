from supertokens_python import get_all_cors_headers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from apis import router


def init_router(_app: FastAPI) -> None:
    _app.include_router(router)


def init_middleware(_app: FastAPI) -> None:
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000"
        ],
        allow_credentials=True,
        allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=["Content-Type"] + get_all_cors_headers(),
    )


def create_app() -> FastAPI:
    _app = FastAPI(
        title="supertokens",
    )
    init_router(_app=_app)
    init_middleware(_app=_app)
    return _app


app = create_app()
