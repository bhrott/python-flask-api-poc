from passlib.hash import pbkdf2_sha256


def verify_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)