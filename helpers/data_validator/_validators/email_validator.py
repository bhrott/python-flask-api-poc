from helpers.models.email import Email
from .string_validator import validate_string


def validate_email(schema, value, ctx):
    validate_string({}, value, ctx)

    email = Email(value)

    if not email.is_valid():
        ctx.error(
            error_code='email',
            message='The value should be a valid email',
            schema=schema,
            value=value
        )
