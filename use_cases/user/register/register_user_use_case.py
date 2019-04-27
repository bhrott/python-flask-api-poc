def register_module(injector):
    def register_user(email, password):
        User = injector.resolve('user')

        db_user = User.find_one({
            'email': email
        })

        InvalidDataError = injector.resolve('invalid_data_error_model')
        translation = injector.resolve('translation')

        if db_user is not None:
            raise InvalidDataError(
                translation.EXCEPTION_USER_ALREADY_EXISTS
            )

        user = User()
        user.email = email
        user.password = password

        saved = User.create(user)

        return saved

    injector.singleton('register_user_use_case', lambda _ : register_user)
