from helpers.translation import translation
from use_cases import UseCase
from entities.user import User
from helpers.models.error import InvalidDataError


class RegisterUserUseCase(UseCase):
    _email = None
    _password = None

    def __init__(self, email, password):
        self._email = email
        self._password = password

    def execute(self):
        db_user = User.find_one({
            'email': self._email
        })

        if db_user is not None:
            raise InvalidDataError(
               translation.get_current().EXCEPTION_USER_ALREADY_EXISTS
            )

        user = User()
        user.email = self._email
        user.password = self._password

        saved = User.create(user)

        return saved
