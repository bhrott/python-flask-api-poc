from flask import Flask
from api.controllers.user import register_user_controller
from api.middlewares import error_handler_middleware

app = Flask(__name__)

error_handler_middleware.init(app)
register_user_controller.init(app)

if __name__ == '__main__':
    app.run(debug=True)
