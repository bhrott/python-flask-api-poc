from passlib.hash import pbkdf2_sha256


class Password:
    def __init__(self, injector):
        pass

    def hash_password(self, password):
        hash = pbkdf2_sha256.hash(password)
        return hash

    def validate_password_rules(self, password):
        # TODO: validate password rules.
        return True, ''

    def verify_password(self, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)


def register_module(injector):
    injector.singleton('password', Password)