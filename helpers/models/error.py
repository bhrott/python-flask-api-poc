from helpers.translation import translation


class Error(Exception):
    def __init__(self, message, code=500, data={}):
        self.code = code
        self.message = message if message else translation.get_current().EXCEPTION_INTERNAL_ERROR
        self.data = data


class InvalidDataError(Error):
    def __init__(self, message, data={}):
        Error.__init__(self, message=message, code=422, data=data)


class UnauthorizedError(Error):
    def __init__(self, data={}):
        Error.__init__(self, message=translation.get_current().EXCEPTION_UNAUTHORIZED, code=401, data=data)


class BadRequestError(Error):
    def __init__(self, message=None, data={}):
        Error.__init__(
            self,
            message=message if message else translation.get_current().EXCEPTION_BAD_REQUEST,
            code=400,
            data=data
        )
