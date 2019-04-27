from flask import request, jsonify
from use_cases.user.register import RegisterUserUseCase


def init_user_register_ctrl(app):
    @app.route('/register', methods=['POST'])
    def user_register_ctrl():
        data = request.get_json()

        register_user = RegisterUserUseCase(
            email=data['email'],
            password=data['password']
        )

        registered = register_user.execute()

        return jsonify({
            'registered': {
                'id': registered.id
            }
        }), 201

