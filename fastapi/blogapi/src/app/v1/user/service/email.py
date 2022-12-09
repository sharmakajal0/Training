from typing import Union
from fastapi import HTTPException, status

from core.utils.token_helper import TokenHelper
from config import config

import smtplib

token_helper = TokenHelper()

async def send_verification(email: str, username: str):
    sender = config.USERNAME
    receiver = email

    password = config.PASSWORD

    token = token_helper.access_token

    message = f"""verify your account with the link below:\n
        <html>
            <a class="btn btn-primary" href="#" role="button">Reset Password</a>
        </html>
    """    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    try:
        server.sendmail(sender, receiver, message)
    except:
        raise HTTPException(status_code=403, detail="email not sent")
    

async def send_email(email: str, otp: Union[str, None]) -> bool:
    sender = config.USERNAME
    receiver = email

    password = config.PASSWORD

    message = f"""Enter the otp below to reset your password\n
                {otp}
    """

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    try:
        server.sendmail(sender, receiver, message)
    except:
        raise HTTPException(status_code=403, detail="email not sent")