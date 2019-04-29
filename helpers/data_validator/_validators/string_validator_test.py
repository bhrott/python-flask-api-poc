import unittest

from ..data_validator import DataValidator, DataValidationError


class TestStringValidator(unittest.TestCase):
    def test_not_string_should_raise_error(self):
        schema = {
            '$type': 'string'
        }
        value = 1

        validator = DataValidator(
            schema=schema,
            value=value
        )

        try:
            validator.validate()
            raise Exception()
        except DataValidationError as ex:
            self.assertEqual('The value should be a string', ex.message)

    def test_value_bigger_than_max_length_should_raise_error(self):
        schema = {
            '$type': 'string',
            'max_length': 4
        }
        value = 'batman'

        validator = DataValidator(
            schema=schema,
            value=value
        )

        try:
            validator.validate()
            raise Exception()
        except DataValidationError as ex:
            self.assertEqual('The value should have less or equal than 4 characters', ex.message)

    def test_value_smaller_than_min_length_should_raise_error(self):
        schema = {
            '$type': 'string',
            'min_length': 10
        }
        value = 'batman'

        validator = DataValidator(
            schema=schema,
            value=value
        )

        try:
            validator.validate()
            raise Exception()
        except DataValidationError as ex:
            self.assertEqual('The value should have more or equal than 10 characters', ex.message)