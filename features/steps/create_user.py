from json import loads

from behave import then, when
from features.page_objects.pages import CreateUser


@when('registrar o usuário')
def user_register(context):
    context.page = CreateUser(context.driver)
    context.cenario_json = loads(context.text)
    context.page.create_user(context.cenario_json)


@then('deverá ser redirecionado para a pagina de "{page}"')
@then('devo ser redirecionado para a pagina de "{page}"')
def check_redirect(context, page):
    assertion_options = {"todo": "/", "register": "register"}
    assert assertion_options.get(page) in context.driver.current_url


@then('o label do Email deverá ser "{label_message}"')
def check_email_label(context, label_message):
    assert context.page.email_label.text == label_message
