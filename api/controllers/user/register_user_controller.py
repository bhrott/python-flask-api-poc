from flask import request, jsonify


def register_module(injector):
    app = injector.resolve('app')

    @app.route('/register', methods=['POST'])
    def user_register_ctrl():
        data = request.get_json()

        register_user = injector.resolve('register_user_use_case')

        registered = register_user(
            email=data['email'],
            password=data['password']
        )

        return jsonify({
            'registered': {
                'id': registered.id
            }
        }), 201
