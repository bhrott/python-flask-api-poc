from passlib.hash import pbkdf2_sha256


def hash_password(password):
    hash = pbkdf2_sha256.hash(password)
    return hash


def validate_password_rules(password):
    # TODO: validate password rules.
    return True, ''


def verify_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)