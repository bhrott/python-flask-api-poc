import jwt
from helpers.config import config

_config = config.get_current()


def encode(payload):
    return jwt.encode(payload, _config.JWT_SECRET, algorithm='HS256').decode('utf-8')


def decode(encoded):
    return jwt.decode(encoded, _config.JWT_SECRET, algorithms=['HS256'])
