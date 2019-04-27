import pymongo

from helpers.db import database
from helpers.password import password_service
from ._db_to_user import map_db_result_to_user
from ._validate_user import validate_user


db_collection = database.get_collection('users')
db_collection.create_index([('email', pymongo.ASCENDING)], unique=True)


class User:
    id = None
    email = None
    password = None

    @staticmethod
    def find_one(query):
        db_result = db_collection.find_one(filter=query)
        return None if db_result is None else map_db_result_to_user(db_result, User())

    @staticmethod
    def create(user):
        validate_user(user)

        db_insert_result = db_collection.insert_one({
            'email': user.email,
            'password': password_service.hash(user.password)
        })

        user.id = str(db_insert_result.inserted_id)

        return user


