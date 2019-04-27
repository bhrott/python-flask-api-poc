from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask
from api.controllers.user import register_user_controller, user_login_controller, get_my_profile_controller
from api.middlewares import error_handler_middleware, logger_middleware


app = Flask(__name__)

error_handler_middleware.init(app)
logger_middleware.init(app)

register_user_controller.init(app)
user_login_controller.init(app)
get_my_profile_controller.init(app)

if __name__ == '__main__':
    app.run(debug=True)
