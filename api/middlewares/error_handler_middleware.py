
def init(app):
    """
    Initialize the default error handling for the api.
    All the errors will be tracked by this middleware
    :param app: the Flask app instance
    """

    @app.errorhandler(Exception)
    def handle_error(e):
        print(e)

        message = 'error'
        code = 500

        if hasattr(e, 'code'):
            code = int(e.code)

        if hasattr(e, 'message'):
            message = e.message

        return message, code