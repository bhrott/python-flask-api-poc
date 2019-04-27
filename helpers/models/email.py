class Email:
    value = None

    def __init__(self, value):
        self.value = value

    def is_valid(self):
        # TODO: validate the email
        if self.value is None:
            return False

        return True