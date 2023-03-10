from typing import Dict, Any
from fastapi import Request, Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param

from supertokens_python.recipe.session.asyncio import get_all_session_handles_for_user, merge_into_access_token_payload, get_session_information

async def some_func():
    # we first get all the session_handles (List[string]) for a user
    session_handles = await get_all_session_handles_for_user("userId")

    for handle in session_handles:
        session_information = await get_session_information(handle)
        if session_information is None:
            continue

        await merge_into_access_token_payload(handle, {'newKey': 'newValue'})

class JWToken(HTTPBearer):
    """
    A class inheriting from :class:`HTTPBearer` to inherit the methods necessary for
    token extraction from the request.
    """

    async def __call__(self, request: Request) -> Dict[str, Any]:
        """
        A magic method intercepts the request and extracts token from it.
        allowing us to access the token in the request context.

        :param request: FastAPI Request.
        :return: Claims included in the token.
        """
        authorization: str = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                # raise NoTokenException
                raise HTTPException(status_code=404, detail="TOkEN NOT FOUND")
        if scheme.lower() != "bearer":
            if self.auto_error:
                # raise InvalidTokenException
                raise HTTPException(status_code=403, detail="INVALID TOKEN")
        return {"Authorization": authorization}


access = JWToken(scheme_name="JWT access token")
refresh = JWToken(scheme_name="JWT refresh token")