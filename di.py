class DI:
    _modules = {}
    _singletons = {}

    def singleton(self, name, resolver):
        def handler(injector):
            if hasattr(self._singletons, name):
                return self._singletons[name]

            instance = resolver(injector)
            self._singletons[name] = instance
            return instance

        self._modules[name] = handler

    def factory(self, name, resolver):
        def handler(injector):
            return resolver(injector)

        self._modules[name] = handler

    def resolve(self, name):
        if name not in self._modules:
            raise Exception(
                'The module {} is not registered'.format(name)
            )

        resolver = self._modules[name]

        return resolver(self)


def register_modules():
    #
    # HELPERS
    #
    from helpers.config import config
    config.register_module(di)

    from helpers.db import database
    database.register_module(di)

    from helpers.models import email, error
    email.register_module(di)
    error.register_module(di)

    from helpers.password import password
    password.register_module(di)

    from helpers.translation import translation
    translation.register_module(di)

    #
    # ENTITIES
    #
    from entities.user import user
    user.register_module(di)

    #
    # USE_CASES
    #
    from use_cases.user.register import register_user_use_case
    register_user_use_case.register_module(di)

    #
    # API MIDDLEWARES
    #
    from api.middlewares import error_handler_middleware
    error_handler_middleware.register_module(di)

    #
    # API CONTROLLERS
    #
    from api.controllers.user import register_user_controller
    register_user_controller.register_module(di)


di = DI()
