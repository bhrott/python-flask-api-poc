from api.controllers.user import register_user_controller, user_login_controller, get_my_profile_controller


def init_controllers(app):
    """
    Register all the controllers for the api
    :param app: the Flask app instance.
    """
    register_user_controller.init(app)
    user_login_controller.init(app)
    get_my_profile_controller.init(app)