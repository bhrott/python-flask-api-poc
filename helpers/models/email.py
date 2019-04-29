import re


_EMAIL_REGEX = "^[_a-z0-9-]+(\\.[_a-z0-9-]+)*@[a-z0-9-]+(\\.[a-z0-9-]+)*(\\.[a-z]{2,4})$"


class Email:
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        if not self.value:
            return False

        if not re.match(_EMAIL_REGEX, self.value):
            return False

        return True
