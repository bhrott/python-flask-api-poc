from flask import request
from helpers.jwt import jwt
from helpers.models.error import UnauthorizedError


def require_logged_user(func):
    def require_logged_user_wrapper():
        authorization = request.headers.get('authorization')

        if not authorization:
            raise UnauthorizedError()

        token = authorization.replace('Bearer ', '')

        try:
            session = jwt.decode(token)
            if not session:
                raise UnauthorizedError()
        except Exception:
            raise UnauthorizedError()

        request.logged_user = session

        return func()

    return require_logged_user_wrapper
