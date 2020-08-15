from behave import given, then, when
from features.helpers.api import create_user
from features.page_objects.pages import Login


@given('que esteja logado')
def default_login(context):
    test_user = {
        'name': 'test',
        'email': 'test@test',
        'password': 'test',
    }

    create_user(context.base_url, test_user)

    if 'todo' not in context.driver.title.lower():
        context.driver.get(context.base_url)
        page = Login(context.driver)
        page.wait_form()

        page.email = test_user['email']
        page.password = test_user['password']
        page.submit.click()


@when('logar com credenciais inválidas')
@when('logar com credenciais válidas')
def invalid_login(context):
    context.page = Login(context.driver)
    context.page.wait_form()
    context.page.email = 'test@test'
    context.page.password = '1234'
    context.page.submit.click()


@then('a mensagem de erro deverá ser exibida')
def invalid_login(context):
    context.page.wait_error_message()

    assert context.page.error.text == context.text


@given('faça logout')
def logout(context):
    context.driver.find_element_by_css_selector('.btn-header').click()
