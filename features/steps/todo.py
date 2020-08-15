from json import loads

from behave import given, then, when
from features.modules.todo import check_stack, table_to_task
from features.page_objects.pages import CreateTodo, Todo


@given('que esteja na página de "{page}"')
def natigate_to_page(context, page):
    pages = {'todo': ''}
    context.driver.get(context.base_url + pages[page])


@when('registrar tarefa')
@when('registrar as tarefas')
def task_register(context):
    page = CreateTodo(context.driver)

    for row in context.table:
        page.name = row['nome']
        page.description = row['descrição']
        if 'urgent' in row:
            page.urgent.click()

        page.submit.click()


@then('a tarefa deve estar na pilha de "{stack}"')
@then('as tarefas devem estar na pilha de "{stack}"')
def check_task_on_stack(context, stack):
    todos = Todo(context.driver)
    tasks = todos.get_tasks()

    table = [table_to_task(row) for row in context.table]

    assert check_stack(tasks, table)


@when('atualizar a página')
def reload_page(context):
    context.driver.refresh()
