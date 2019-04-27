import os


class Config:
    DB_CONNECTION = os.getenv('DB_CONNECTION')
    DB_DATABASE_DEFAULT = 'python-api'


class ConfigDev(Config):
    pass


class ConfigQA(Config):
    pass


class ConfigProd(Config):
    pass


def get_current():
    return ConfigDev

