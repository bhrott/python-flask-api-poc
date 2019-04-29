from .translation_base import TranslationBase


class EnUs(TranslationBase):
    EXCEPTION_INTERNAL_ERROR = 'Ooops! Something wrong happened! Please try again later'
    EXCEPTION_REQUIRED_EMAIL = 'The email is required'
    EXCEPTION_USER_ALREADY_EXISTS = 'The user already exists'
    EXCEPTION_PASSWORD_RULES_NOT_MATCH = 'The password is weak'
    EXCEPTION_INVALID_CREDENTIALS = 'Invalid credentials'
    EXCEPTION_UNAUTHORIZED = 'Unauthorized'
    EXCEPTION_BAD_REQUEST = 'The provided data is not valid'
