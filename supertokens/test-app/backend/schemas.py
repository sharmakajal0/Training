from pydantic import BaseModel, EmailStr, validators


class AuthSignIn(BaseModel):

    email: EmailStr = None
    phoneNumber: str = None


class AuthSignInReuse(BaseModel):

    deviceId: str
    preAuthSessionId: str


class AuthSignInConsume(BaseModel):

    deviceId: str
    preAuthSessionId: str
    userInputCode: str


class AuthSignInCodeResend(BaseModel):

    deviceId: str
    preAuthSessionId: str
    otp: str

class AuthSignUp(BaseModel):

    value: EmailStr

class FormFields(BaseModel):

    formFields: list[AuthSignUp]