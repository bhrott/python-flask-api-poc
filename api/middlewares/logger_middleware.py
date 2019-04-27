from flask import request
from helpers.config import config


def init(app):
    @app.before_request
    def logger_middleware_wrapper():
        if config.get_current().DEBUG:
            print('----------------------------')
            print('REQUEST')
            print('{}: {}'.format(request.method, request.url))
            print('headers: {}'.format(request.headers))
            print('json: {}'.format(request.get_json()))
            print('----------------------------')
