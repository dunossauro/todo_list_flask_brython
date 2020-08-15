from behave import then, when
from features.page_objects.pages import CreateUser


@when('registrar minha conta')
def user_register(context):
    context.page = CreateUser(context.driver)
    for row in context.table:
        context.page.create_user(
            row['nome'], row['email'], row['senha'],
        )


@then('deverá ser redirecionado para a pagina de "{page}"')
@then('devo ser redirecionado para a pagina de "{page}"')
def check_redirect(context, page):
    assertion_options = {"todo": "/", "register": "register"}
    assert assertion_options.get(page) in context.driver.current_url


@then('o label do Email deverá ser "{label_message}"')
def check_email_label(context, label_message):
    assert context.page.email_label.text == label_message
