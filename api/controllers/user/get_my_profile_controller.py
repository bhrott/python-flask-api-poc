from flask import request, jsonify
from api.middlewares.require_logged_user_middleware import require_logged_user


def init(app):
    @app.route('/profile', methods=['GET'])
    @require_logged_user
    def get_my_profile_controller():
        return jsonify({
            'profile': request.logged_user
        })

