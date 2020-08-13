from ipdb import spost_mortem
from selenium.webdriver import Firefox


def before_all(context):
    context.driver = Firefox()
    context.base_url = context.config.userdata.get('base_url')


def after_step(context, step):
    if context.config.userdata.getbool('debug'):
        spost_mortem(step.exc_traceback)


def after_all(context):
    context.driver.quit()
