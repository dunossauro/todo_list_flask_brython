from ipdb import spost_mortem
from selenium.webdriver import Chrome, Firefox, Safari


def before_all(context):
    BROWSERS_CAPABILITIES = {
        'chrome': Chrome,
        'firefox': Firefox,
        'safari': Safari
    }
    context.driver = BROWSERS_CAPABILITIES.get(
        context.config.userdata.get('browser').lower()
    )()
    context.base_url = context.config.userdata.get('base_url')


def after_step(context, step):
    if context.config.userdata.getbool('debug'):
        spost_mortem(step.exc_traceback)


def after_all(context):
    context.driver.quit()
