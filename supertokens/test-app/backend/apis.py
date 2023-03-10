from fastapi import APIRouter, status, Depends
from schemas import AuthSignIn, AuthSignInConsume, AuthSignInCodeResend
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session
from httpx import AsyncClient
from session import access
from supertokens_python.recipe.session.asyncio import get_session
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse
from fastapi.responses import RedirectResponse
from supertokens_python.recipe.session.exceptions import (
    UnauthorisedError,
    TryRefreshTokenError
)


router = APIRouter()

client = AsyncClient()

headers = {
    "Access-Control-Allow-Credentials": "True",
    "accept": "application/json",
    "content-type": "application/json",
    "rid": "thirdpartypasswordless",
    "st-auth-mode": "cookie"
}


@router.post(
    "/auth/signin/code",
    status_code=status.HTTP_200_OK,
    name="Create User"
    )
async def create_user(request: AuthSignIn):
    url = "http://localhost:8000/auth/signinup/code"
    payload = {'email': request.email}
    if request.email is None:
        payload = {
            "phoneNumber": request.phoneNumber
        }
    elif request.phoneNumber is None:
        payload = {
            "email": request.email
        }
    result = await client.post(url=url, headers=headers, json=payload)
    return result.json()


@router.post(
    "/auth/signinup/code/resend",
    status_code=status.HTTP_200_OK,
    name="Resend Code",
)
async def create_resend_code(request: AuthSignInCodeResend):
    url = "http://127.0.0.1:8000/auth/signinup/code/resend"
    result = await client.post(url=url, headers=headers, json={
        "deviceId": request.deviceId,
        "preAuthSessionId": request.preAuthSessionId,
        "otp": request.otp
    })
    return result.json()


@router.post("/auth/signinup/code/consume", status_code=status.HTTP_200_OK, name="Consume Code")
async def consume_code(request: AuthSignInConsume):
    url="http://127.0.0.1:8000/auth/signinup/code/consume"
    result = await client.post(
        url=url,
        headers=headers,
        json={
            "deviceId": request.deviceId,
            "preAuthSessionId": request.preAuthSessionId,
            "userInputCode": request.userInputCode
        }
    )

    return result.headers['sAccessToken']


@router.get("/auth/signup/email/exists", status_code=status.HTTP_200_OK, name="email exists")
async def email_exists(email: str):
    url="http://127.0.0.1:8000/auth/signup/email/exists"
    result = await client.get(
        url=url,
        headers=headers,
        params={"email": email}
    )
    return result.json()


@router.get("/auth/signup/phonenumber/exists")
async def phone_exists(phoneNumber: str):
    url="http://127.0.0.1:8000/auth/signup/phonenumber/exists"
    result = await client.get(
        url=url,
        headers=headers,
        params={"phoneNumber": phoneNumber}
    )

    return result.json()

@router.post('/like_comment')
async def like_comment(session: SessionContainer = Depends(verify_session()), token=Depends(access)):
    user_id = session.get_user_id()

    return user_id


@router.get('/dashboard')  
async def dashboard(request: Request):
    try:
        session = await get_session(request, override_global_claim_validators=lambda global_validators, session, user_context: [])

        if session is None:
            raise Exception("Should never come here")

        user_id = session.get_user_id()

        print(user_id)
        # TODO
    except Exception as e:
        if isinstance(e, TryRefreshTokenError) or isinstance(e, UnauthorisedError):
            return RedirectResponse(
                '/refresh-session?redirectBack=/dashboard',
                status_code=302)
        raise e

@router.post('/update_info') 
async def update_info(session: SessionContainer = Depends(verify_session())):
    await session.merge_into_access_token_payload({'newKey': 'newValue'})

    return PlainTextResponse(content='success')

@router.get("/getJWT")
async def get_jwt(session: SessionContainer = Depends(verify_session())):
    current_jwt = session.get_access_token_payload()['jwt']

    print(current_jwt)
