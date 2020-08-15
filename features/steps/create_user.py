from json import loads

from behave import then, when
from features.page_objects.pages import CreateUser


@when('registrar o usuário')
def user_register(context):
    page = CreateUser(context.driver)
    context.cenario_json = loads(context.text)
    page.create_user(context.cenario_json)


@then('deverá ser redirecionado para a pagina de "{page}"')
def check_redirect(context, page):
    assertion_options = {"todo": "/", "register": "register"}
    assert assertion_options.get(page) in context.driver.current_url


@then('o label do Email deverá ser "{label_message}"')
def check_email_label(context, label_message):
    page = CreateUser(context.driver, label_message)
    assert page.email_label.text == label_message
