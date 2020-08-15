from os import environ


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SECRET_KEY = 'batatinhafritasvoadoras123'


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
