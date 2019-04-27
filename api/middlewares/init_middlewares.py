from api.middlewares import error_handler_middleware, logger_middleware


def init_middlewares(app):
    """
    Init the global route middlewares.
    :param app: the Flask app instance
    """
    error_handler_middleware.init(app)
    logger_middleware.init(app)