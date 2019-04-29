from flask import request, jsonify
from use_cases.user.user_login_use_case import login_user
from api.middlewares.request_validator_middleware import validate_request


def init(app):
    @app.route('/login', methods=['POST'])
    @validate_request(
        schema={
            '$type': 'dict',
            'props': {
                'email': {
                    '$type': 'email'
                },
                'password': {
                    '$type': 'string'
                }
            }
        },
        json=True
    )
    def user_login_ctrl():
        data = request.get_json()

        session = login_user(
            email=data['email'],
            password=data['password']
        )

        return jsonify(session), 200

