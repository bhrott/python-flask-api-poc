from helpers.translation.translation_codes import TranslationCodes


class Error(Exception):
    code = 500
    message = TranslationCodes.EXCEPTION_INTERNAL_ERROR
    data = {}

    def __init__(self, message, code=500, data={}):
        self.code = code
        self.message = message
        self.data = data


class InvalidDataError(Error):
    def __init__(self, message, data={}):
        Error.__init__(self, message=message, code=422, data=data)


class UnauthorizedError(Error):
    def __init__(self, message, data={}):
        Error.__init__(self, message=message, code=401, data=data)
