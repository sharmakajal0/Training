from datetime import datetime, timedelta
from typing import NoReturn, Union

import jwt

from config import config
from core.exceptions import DecodeTokenException, ExpiredTokenException


class TokenHelper:
    access_token = ''

    @staticmethod
    def encode(username: str, expire_period: int = 3600) -> str:
        payload = {
            'exp' : datetime.utcnow() + timedelta(days=0, minutes=30),
            'iat' : datetime.utcnow(),
	        'scope': 'access_token',
            'sub' : username
        }
        return jwt.encode(
            payload,
            config.SECRET_KEY,
            algorithm=config.JWT_ALGORITHM
        )

    @staticmethod
    def decode(token: str):
        try:
            payload = jwt.decode(token, config.SECRET_KEY, algorithms='HS256')
            if (payload['scope'] == 'access_token'):
                return payload['sub']   
        except jwt.ExpiredSignatureError:
            raise ExpiredTokenException
        except jwt.InvalidTokenError:
            raise DecodeTokenException

    @staticmethod
    def decode_expired_token(token: str) -> Union[dict, NoReturn]:
        try:
            return jwt.decode(
                token,
                config.SECRET_KEY,
                config.JWT_ALGORITHM,
                options={"verify_exp": False},
            )
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException
