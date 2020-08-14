from behave import given
from features.page_objects.pages import Login


@given('que esteja logado')
def default_login(context):
    context.driver.get(context.base_url)
    page = Login(context.driver)
    page.wait_form()

    page.email = 'test@test'
    page.password = '1234'
    page.submit.click()
