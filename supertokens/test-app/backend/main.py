from supertokens_python import init, InputAppInfo, SupertokensConfig, get_all_cors_headers
from supertokens_python.recipe.thirdpartypasswordless import Google
from supertokens_python.recipe import thirdpartypasswordless, session, dashboard
from supertokens_python.recipe.session.interfaces import RecipeInterface

from supertokens_python.recipe.passwordless import ContactEmailOrPhoneConfig

from fastapi import FastAPI
from typing import Dict, Any, Union
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware

from apis import router


def override_functions(original_implementation: RecipeInterface):
    original_implementation_create_new_session = original_implementation.create_new_session

    async def create_new_session(request: Any, user_id: str,
                                 access_token_payload: Union[None, Dict[str, Any]],
                                 session_data: Union[None, Dict[str, Any]], user_context: Dict[str, Any]):

        if access_token_payload is None:
            access_token_payload = {}

        access_token_payload['role'] = 'user'

        return await original_implementation_create_new_session(request, user_id, access_token_payload, session_data, user_context)

    original_implementation.create_new_session = create_new_session
    return original_implementation

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
        connection_uri="http://localhost:3567",
        # api_key=<API_KEY(if configured)>
    ),
    framework='fastapi',
    recipe_list=[
        session.init(
            jwt=session.JWTConfig(
                enable=True
            ),
            override=session.InputOverrideConfig(functions=override_functions)
        ), # initializes session features
        dashboard.init(api_key="chandan123"),
        thirdpartypasswordless.init(
            # email_delivery=EmailDeliveryConfig(override=custom_email_delivery),
            flow_type="USER_INPUT_CODE",
            contact_config=ContactEmailOrPhoneConfig(),
            providers=[
                Google(
                    client_id='1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com',
                    client_secret='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'
                    # ), Facebook(
                    #     client_id='FACEBOOK_CLIENT_ID',
                    #     client_secret='FACEBOOK_CLIENT_SECRET'
                )
            ],
        ),
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
