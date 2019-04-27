from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask
from api.controllers.init_controllers import init_controllers
from api.middlewares.init_middlewares import init_middlewares
from helpers.config import config

_config = config.get_current()

app = Flask(__name__)

init_middlewares(app)
init_controllers(app)

#
# run
#
if __name__ == '__main__':
    app.run(debug=_config.DEBUG)
