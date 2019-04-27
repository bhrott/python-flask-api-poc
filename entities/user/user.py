import pymongo


def register_module(injector):
    def map_db_result_to_user(db_result, user):
        user.id = db_result['_id']
        user.email = db_result['email']
        user.password = db_result['password']

        return user

    def validate_user(user):
        Email = injector.resolve('email_model')
        InvalidDataError = injector.resolve('invalid_data_error_model')
        translation = injector.resolve('translation')
        password = injector.resolve('password')

        email_model = Email(user.email)

        if email_model.is_valid() is False:
            raise InvalidDataError(
                message=translation.EXCEPTION_REQUIRED_EMAIL
            )

        is_password_valid, password_validation_message = password.validate_password_rules(user.password)

        if is_password_valid is False:
            raise InvalidDataError(
                message=password_validation_message
            )

    def handler():
        database = injector.resolve('database')
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

                password = injector.resolve('password')

                db_insert_result = db_collection.insert_one({
                    'email': user.email,
                    'password': password.hash_password(user.password)
                })

                user.id = str(db_insert_result.inserted_id)

                return user

        return User

    injector.singleton('user', lambda _: handler())





