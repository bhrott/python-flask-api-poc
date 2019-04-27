from pymongo import MongoClient


class Database:
    _config = None
    _mongo_client = None
    _default_db_name = None

    def __init__(self, injector):
        self._config = injector.resolve('config')
        self._mongo_client = MongoClient(
            self._config.DB_CONNECTION
        )
        self._default_db_name = self._config.DB_DATABASE_DEFAULT

    def set_default_db(self, db_name):
        self._default_db_name = db_name

    def get_client(self):
        return self._mongo_client

    def get_db(self, db_name):
        return self._mongo_client[db_name]

    def get_collection(self, collection_name, db_name=None):
        selected_db_name = db_name if db_name is not None else self._default_db_name

        db = self.get_db(selected_db_name)

        return db[collection_name]


def register_module(injector):
    injector.singleton('database', Database)


