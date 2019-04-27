from flask import request, jsonify
from use_cases.user.register_user_use_case import register_user


def init(app):
    @app.route('/register', methods=['POST'])
    def user_register_ctrl():
        data = request.get_json()

        registered = register_user(
            email=data['email'],
            password=data['password']
        )

        return jsonify({
            'registered': {
                'id': registered.id
            }
        }), 201

