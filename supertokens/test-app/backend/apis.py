from fastapi import APIRouter, status, Depends
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from supertokens_python.recipe.session.asyncio import get_session
from supertokens_python.recipe.session.exceptions import (
    UnauthorisedError,
    TryRefreshTokenError
)
from supertokens_python.recipe.session.exceptions import raise_invalid_claims_exception, ClaimValidationError
from schemas import AuthSignIn, AuthSignInConsume, AuthSignInCodeResend
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.userroles import UserRoleClaim
from supertokens_python.recipe.session.framework.fastapi import verify_session
from fastapi.responses import PlainTextResponse
from httpx import AsyncClient
from typing import Union, Dict, Any


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
    "/request_otp",
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


@router.post("/verify_otp",
                 status_code=status.HTTP_200_OK,
                 response_model=None,
                 response_description="",
                 name="Verify OTP", )
async def login(request: AuthSignInConsume) -> Union[Dict, Any]:
    url="http://127.0.0.1:8000/auth/signinup/code/consume"
    payload = {
        "userInputCode": request.userInputCode,
        "deviceId": request.deviceId,
        "preAuthSessionId": request.preAuthSessionId, }
    response = await client.post(url=url, headers=headers, json=payload)
    access_token = response.cookies.get("st-access-token")


    if access_token:
        return JSONResponse(content={
            "sAccessToken": response.cookies.get("st-access-token").replace('"', ""),
            "sRefreshToken": response.cookies.get("st-refresh-token").replace('"', ""),
            "sIdRefreshToken": response.cookies.get("st-refresh-token").replace('"', "")}
        )

    else:
        return response.json()

@router.get("/check_email", status_code=status.HTTP_200_OK, name="email exists")
async def email_exists(email: str):
    url="http://127.0.0.1:8000/auth/signup/email/exists"
    result = await client.get(
        url=url,
        headers=headers,
        params={"email": email}
    )
    return result.json()


@router.get("/check_phone")
async def phone_exists(phoneNumber: str):
    url="http://127.0.0.1:8000/auth/signup/phonenumber/exists"
    result = await client.get(
        url=url,
        headers=headers,
        params={"phoneNumber": phoneNumber}
    )

    return result.json()

@router.post('/like_comment')
async def like_comment(request: Request):
    session = await get_session(request)

    if session is None:
        raise Exception("Should never come here")
    
    user_id = await session.get_expiry()
    
    print(user_id)
    return user_id

@router.get('/dashboard')  
async def dashboard(request: Request):
    try:
        session = await get_session(request, override_global_claim_validators=lambda global_validators, session, user_context: [])

        if session is None:
            raise Exception("Should never come here")

        user_id = session.get_user_id()

        return user_id
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

@router.get('/get_jwt') 
async def get_jwt(session: SessionContainer = Depends(verify_session())):
    current_jwt = session.get_access_token_payload()['jwt']

    print(current_jwt)
    return current_jwt


@router.post('/update-access-token-payload') 
async def merge_into_access_token_payload(session: SessionContainer = Depends(verify_session())):
    await session.merge_into_access_token_payload({ 'newKey': 'newValue' })

    return PlainTextResponse(content='success')

@router.get('/my_api') 
async def my_api(session: SessionContainer = Depends(verify_session())):
    access_token_payload = session.get_access_token_payload()

    custom_claim_value = access_token_payload.get('customClaim', None)

    print(custom_claim_value)
    return custom_claim_value

@router.get('/update-blog')
async def update_blog_api(session: SessionContainer = Depends(verify_session())):
    roles = await session.get_claim_value(UserRoleClaim)
    if roles is None or "admin" not in roles:
        raise_invalid_claims_exception("User is not an admin", [ClaimValidationError(UserRoleClaim.key, None)])

@router.get('/logout')
async def revoke_session(session: SessionContainer = Depends(verify_session())):
    await session.revoke_session()
    return PlainTextResponse(content="success")
