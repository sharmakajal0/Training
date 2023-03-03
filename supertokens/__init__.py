from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import thirdpartypasswordless, session
from supertokens_python.recipe.thirdpartypasswordless import Google, Github, Apple

from supertokens_python.recipe.passwordless import ContactEmailOnlyConfig
init(
    app_info=InputAppInfo(
        app_name="supertoken-passwordless",
        api_domain="http://localhost:5050",
        website_domain="http://localhost:3000",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        # https://try.supertokens.com is for demo purposes. Replace this with the address of your core instance (sign up on supertokens.com), or self host a core.
        connection_uri="https://try.supertokens.com",
        # api_key=<API_KEY(if configured)>
    ),
    framework='fastapi',
    recipe_list=[
        session.init(), # initializes session features
        thirdpartypasswordless.init(
            flow_type="MAGIC_LINK",
            contact_config=ContactEmailOnlyConfig(),
            # TODO: See next steps for third party provider setup 
            providers=[
                # We have provided you with development keys which you can use for testing.
                # IMPORTANT: Please replace them with your own OAuth keys for production use.
                Google(
                    client_id='1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com',
                    client_secret='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'
                # ), Facebook(
                #     client_id='FACEBOOK_CLIENT_ID',
                #     client_secret='FACEBOOK_CLIENT_SECRET'
                ), Github(
                    client_id='467101b197249757c71f',
                    client_secret='e97051221f4b6426e8fe8d51486396703012f5bd'
                ),
                Apple(
                    client_id="4398792-io.supertokens.example.service",
                    client_key_id="7M48Y4RYDL",
                    client_private_key="-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgu8gXs+XYkqXD6Ala9Sf/iJXzhbwcoG5dMh1OonpdJUmgCgYIKoZIzj0DAQehRANCAASfrvlFbFCYqn3I2zeknYXLwtH30JuOKestDbSfZYxZNMqhF/OzdZFTV0zc5u5s3eN+oCWbnvl0hM+9IW0UlkdA\n-----END PRIVATE KEY-----",
                    client_team_id="YWQCXGJRJL"
                )
            ]
        )
    ],
    mode='asgi' # use wsgi if you are running using gunicorn
)