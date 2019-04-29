from ._validators.string_validator import validate_string
from ._validators.dict_validator import validate_dict
from ._validators.list_validator import validate_list
from ._validators.email_validator import validate_email


class DataValidationError(Exception):
    def __init__(self, error_path, error_type, message, extra={}):
        self.error_path = error_path
        self.message = message
        self.error_type = error_type
        self.extra = extra


class DataValidator:
    validators = {
        'string': validate_string,
        'dict': validate_dict,
        'list': validate_list,
        'email': validate_email
    }

    def __init__(self, schema, value):
        self.schema = schema
        self.value = value

        self.path = ['$root']

    def validate(self):
        schema_type = self.schema['$type']
        validator = self.validators[schema_type]

        validator(
            schema=self.schema,
            value=self.value,
            ctx=self
        )

    def error(self, error_type, message, extra={}):
        raise DataValidationError(
            error_path='>'.join(self.path),
            error_type=error_type,
            message=message,
            extra=extra
        )

    def add_to_path(self, path):
        self.path.append(path)

    def pop_path(self):
        self.path.pop()
