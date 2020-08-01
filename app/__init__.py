from flask import Flask


def create_app():
    app = Flask('app')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    from .home import home
    app.register_blueprint(home)

    from .api import api
    app.register_blueprint(api)

    from .front import front
    app.register_blueprint(front)

    from .model import configure as model_conf
    model_conf(app)

    from .serializer import configure as serial_conf
    serial_conf(app)

    return app
