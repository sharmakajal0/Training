from supertokens_python import init, InputAppInfo, SupertokensConfig, get_all_cors_headers
from supertokens_python.recipe import passwordless, session, dashboard

from supertokens_python.recipe.passwordless import ContactEmailOrPhoneConfig

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware

from apis import router

init(
    app_info=InputAppInfo(
        app_name="fastapi-react",
        api_domain="http://localhost:8000",
        website_domain="http://localhost:3000",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        # https://try.supertokens.com is for demo purposes. Replace this with the address of your core instance (sign up on supertokens.com), or self host a core.
        connection_uri="http://localhost:3567/",
        # api_key=<API_KEY(if configured)>
    ),
    framework='fastapi',
    recipe_list=[
        session.init(), # initializes session features
        passwordless.init(
            flow_type="USER_INPUT_CODE",
            contact_config=ContactEmailOrPhoneConfig()
        ),
        dashboard.init(api_key="kajalkajal")
    ],
    mode='asgi' # use wsgi if you are running using gunicorn
)

app = FastAPI()
app.include_router(router)
app.add_middleware(get_middleware())


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)
