from helpers.models import Email, InvalidDataError
from helpers.translation.translation_codes import TranslationCodes
from helpers.password import validate_password_rules


def validate_user(user):
    email_model = Email(user.email)

    if email_model.is_valid() is False:
        raise InvalidDataError(
            message=TranslationCodes.EXCEPTION_REQUIRED_EMAIL
        )

    password_validation = validate_password_rules(user.password)

    if password_validation.valid is False:
        raise InvalidDataError(
            message=password_validation.message
        )