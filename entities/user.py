import pymongo

from helpers.db import database
from helpers.password import password
from helpers.models.email import Email
from helpers.models.error import InvalidDataError
from helpers.translation import translation


db_collection = database.get_current().get_collection('users')
db_collection.create_index([('email', pymongo.ASCENDING)], unique=True)


def _validate_user(user):
    email_model = Email(user.email)

    if email_model.is_valid() is False:
        raise InvalidDataError(
            message=translation.EXCEPTION_REQUIRED_EMAIL
        )

    pass_is_valid, pass_message = password.validate_password_rules(user.password)

    if pass_is_valid is False:
        raise InvalidDataError(
            message=pass_message
        )


def _map_db_result_to_user(db_result, user):
    user.id = str(db_result['_id'])
    user.email = db_result['email']
    user.password = db_result['password']

    return user


class User:
    def __init__(self):
        self.id = None
        self.email = None
        self.password = None

    @staticmethod
    def find_one(query):
        db_result = db_collection.find_one(filter=query)
        return None if db_result is None else _map_db_result_to_user(db_result, User())

    @staticmethod
    def create(user):
        _validate_user(user)

        db_insert_result = db_collection.insert_one({
            'email': user.email,
            'password': password.hash_password(user.password)
        })

        user.id = str(db_insert_result.inserted_id)

        return user


