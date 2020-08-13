from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask('app')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SECRET_KEY'] = 'batatinhafritasvoadoras123'

    login_manager = LoginManager(app)
    login_manager.login_view = 'front.login'

    from .api import api
    app.register_blueprint(api)

    from .front import front
    app.register_blueprint(front)

    from .model import User
    from .model import configure as model_conf
    model_conf(app)

    from .serializer import configure as serial_conf
    serial_conf(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
