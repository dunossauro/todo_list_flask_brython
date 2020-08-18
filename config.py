from os import environ


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = environ.get(
        'DATABASE_URL', default='sqlite:////tmp/test.db'
    )
    SECRET_KEY = environ.get('SECRET', default='batatinhafritasvoadoras123')


class Testing(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = False


class Production(BaseConfig):
    ...


class Development(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    PROPAGATE_EXCEPTIONS = True


envs = {
    'config': BaseConfig,
    'development': Development,
    'production': Production,
    'testing': Testing,
}


def get_env():
    """Choose env class name."""
    return envs[environ.get('FLASK_ENV', default='production')]
