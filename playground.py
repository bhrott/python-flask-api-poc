from helpers.data_validator.data_validator import DataValidator, DataValidationError


schema = {
    '$type': 'dict',
    'props': {
        'hero': {
            '$type': 'dict',
            'props': {
                'name': {
                    '$type': 'string',
                    'max_length': 10,
                    'error_message': 'Invalid Name'
                },
                'weapons': {
                    '$type': 'list',
                    'item_schema': {
                        '$type': 'string',
                        'max_length': 4
                    }
                }
            }
        }
    }
}

value = {
    'hero': {
        'name': 'ben-hur',
        'weapons': [
            'hammer'
        ]
    }
}

try:
    validator = DataValidator(schema, value)
    validator.validate()
    print(True)
except DataValidationError as ex:
    print(ex)





