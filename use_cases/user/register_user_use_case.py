from helpers.translation import translation
from entities.user import User
from helpers.models.error import InvalidDataError


def register_user(email, password):
    db_user = User.find_one({
        'email': email
    })

    if db_user is not None:
        raise InvalidDataError(
            translation.get_current().EXCEPTION_USER_ALREADY_EXISTS
        )

    user = User()
    user.email = email
    user.password = password

    saved = User.create(user)

    return saved
