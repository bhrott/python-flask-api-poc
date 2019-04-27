from flask import Flask
from api.controllers.user.register_user_controller import init_user_register_ctrl
from api.middlewares import init_error_handler

app = Flask(__name__)

init_error_handler(app)

init_user_register_ctrl(app)

if __name__ == '__main__':
    app.run(debug=True)
