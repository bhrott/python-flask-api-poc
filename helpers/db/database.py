from pymongo import MongoClient
from helpers.config import get_current_config


config = get_current_config()


class Database:
    _mongo_client = None
    _default_db = config.DB_DATABASE_DEFAULT

    def __init__(self):
        self._mongo_client = MongoClient(
            config.DB_CONNECTION
        )

    def set_default_db(self, db_name):
        self._default_db = db_name

    def get_client(self):
        return self._mongo_client

    def get_db(self, db_name):
        return self._mongo_client[db_name]

    def get_collection(self, collection_name, db_name=None):
        selected_db_name = db_name if db_name is not None else self._default_db

        db = self.get_db(selected_db_name)

        return db[collection_name]


database = Database()


