from pydantic import BaseModel, EmailStr, validator


class AuthSignIn(BaseModel):

    email: EmailStr = None
    phoneNumber: str = None

    @validator("phoneNumber")
    def email_and_phone_validator(cls, v, values, **kwargs):
        if 'email' in values and v == 'phoneNumber':
            raise ValueError('cannot have both fields')
        return v


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