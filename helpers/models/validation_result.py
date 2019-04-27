class ValidationResult:
    valid = False
    message = ''

    def __init__(self, valid, message=''):
        self.valid = valid
        self.message = message