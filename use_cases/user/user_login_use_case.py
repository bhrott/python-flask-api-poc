from helpers.translation import translation
from entities.user import User
from helpers.models.error import InvalidDataError
from helpers.password import password as pass_service
from helpers.jwt import jwt


def login_user(email, password):
    db_user = User.find_one({
        'email': email
    })

    if db_user is None:
        raise InvalidDataError(
            translation.get_current().EXCEPTION_INVALID_CREDENTIALS
        )

    if not pass_service.verify_password(password, db_user.password):
        raise InvalidDataError(
            translation.get_current().EXCEPTION_INVALID_CREDENTIALS
        )

    access_token = jwt.encode({
        'id': db_user.id,
        'email': db_user.email
    })
    return {
        'id': db_user.id,
        'email': db_user.email,
        'access_token': access_token
    }
