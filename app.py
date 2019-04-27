from flask import Flask
from di import di, register_modules

app = Flask(__name__)

di.singleton('app', lambda injector: app)

register_modules()

if __name__ == '__main__':
    app.run(debug=True)
