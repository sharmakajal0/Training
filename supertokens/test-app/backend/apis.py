from fastapi import APIRouter, status
from schemas import AuthSignIn, AuthSignInConsume, AuthSignInCodeResend, FormFields
from httpx import AsyncClient

router = APIRouter()

client = AsyncClient()


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
    result = await client.post(url=url, json=payload)
    return result.json()


@router.post(
    "/auth/signinup/code/resend",
    status_code=status.HTTP_200_OK,
    name="Resend Code",
)
async def create_resend_code(request: AuthSignInCodeResend):
    url = "http://127.0.0.1:8000/auth/signinup/code/resend"
    result = await client.post(url=url, json={
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
        json={
            "linkCode": request.linkCode,
            "preAuthSessionId": request.preAuthSessionId,
            "userInputCode": request.userInputCode
        }
    )
    return result.json()


@router.get("/auth/signup/email/exists", status_code=status.HTTP_200_OK, name="email exists")
async def email_exists(email: str):
    url="http://127.0.0.1:8000/auth/signup/email/exists"
    result = await client.get(
        url=url,
        params={"email": email}
    )
    return result.json()


@router.get("/auth/signup/phonenumber/exists")
async def phone_exists(phoneNumber: str):
    url="http://127.0.0.1:8000/auth/signup/phonenumber/exists"
    result = await client.get(
        url=url,
        params={"phoneNumber": phoneNumber}
    )

    return result.json()


@router.post("/auth/signinup", status_code=status.HTTP_200_OK, name="sign up")
async def signup(request: FormFields):
    url="http://127.0.0.1:8000/auth/signinup"
    result = await client.post(
        url=url,
        json={
            "formFields": [
                {
                    "value": request.value
                }
            ]
        }
    )
    return result.json()
