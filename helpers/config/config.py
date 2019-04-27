import os


class Config:
    DB_CONNECTION = os.getenv('DB_CONNECTION')
    DB_DATABASE_DEFAULT = 'python-api'
    DEBUG = True
    JWT_SECRET = os.getenv('JWT_SECRET')
    ENV_NAME = os.getenv('ENV_NAME')


class ConfigDev(Config):
    pass


class ConfigQA(Config):
    DEBUG = False


class ConfigProd(Config):
    DEBUG = False


_configs = {
    'local': Config,
    'dev': ConfigDev,
    'qa': ConfigQA,
    'prod': ConfigProd
}


def get_current():
    env_name = os.getenv('ENV_NAME')
    return _configs[env_name]

