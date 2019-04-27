from flask import request, jsonify
from use_cases.user.user_login_use_case import login_user


def init(app):
    @app.route('/login', methods=['POST'])
    def user_login_ctrl():
        data = request.get_json()

        session = login_user(
            email=data['email'],
            password=data['password']
        )

        return jsonify(session), 200

