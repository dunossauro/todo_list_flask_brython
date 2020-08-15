from features.helpers.api import clean_test_database, create_user
from ipdb import spost_mortem
from selenium.webdriver import Firefox


def before_all(context):
    context.base_url = context.config.userdata.get('base_url')


def before_feature(context, feature):
    context.driver = Firefox()


def after_feature(context, feature):
    context.driver.quit()


def before_scenario(context, scenario):
    clean_test_database(context.base_url)
    if 'criar_usuario' in scenario.tags:
        create_user(
            context.base_url,
            {'name': 'test', 'email': 'test@test', 'password': '1234'},
            [201],
        )


def after_step(context, step):
    if context.config.userdata.getbool('debug'):
        spost_mortem(step.exc_traceback)
