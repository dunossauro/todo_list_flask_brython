from behave import given, when, then
from json import loads
from features.page_objects.pages import CreateTodo, Todo


@given('que esteja na página de "{page}"')
def natigate_to_page(context, page):
    context.driver.get(context.base_url + page)


@when('registrar tarefa')
def task_register(context):
    page = CreateTodo(context.driver)
    context.cenario_json = loads(context.text)

    page.name = context.cenario_json['nome']
    page.description = context.cenario_json['description']

    if 'urgent' in context.cenario_json:
        page.urgent.click()

    page.submit.click()


@then('a tarefa deve estar na pilha de "{stack}"')
def check_task_on_stack(context, stack):
    todos = Todo(context.driver)
    tasks = todos.get_tasks()
    for task in tasks:
        if task.name == context.cenario_json['nome']:
            break
    else:
        assert False
