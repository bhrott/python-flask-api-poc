from pymongo import MongoClient


class Database:
    _mongo_client = None
    _default_db = 'python-api'

    def __init__(self):
        self._mongo_client = MongoClient('mongodb://localhost:27017/')

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


