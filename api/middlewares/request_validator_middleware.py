from flask import request
from helpers.models.error import BadRequestError
from helpers.data_validator.data_validator import DataValidationError, DataValidator
from helpers.config import config

_config = config.get_current()


def _validate(schema, value):
    try:
        validator = DataValidator(
            schema=schema,
            value=value
        )
        validator.validate()
    except DataValidationError as ex:
        if _config.DEBUG:
            print(
                ex.__dict__
            )

        raise BadRequestError()


def validate_request(schema, json=False):
    def wrap(fn):
        def middleware():
            if json:
                data = request.get_json()
                _validate(schema, data)

            return fn()

        return middleware
    return wrap
