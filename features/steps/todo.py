from json import loads

from behave import given, then, when
from features.modules.todo import check_stack, table_to_task, task
from features.page_objects.pages import CreateTodo, Doing, Done, Todo


@given('que esteja na página de "{page}"')
def natigate_to_page(context, page):
    pages = {'todo': '', 'register': 'register', 'login': 'login'}
    context.driver.get(context.base_url + pages[page])


@when('criar tarefa')
@when('criar as tarefas')
def task_register(context):
    """Registra uma ou mais tarefas usando a tabela do Gherking."""
    page = CreateTodo(context.driver)

    for row in context.table:
        page.create_todo(row['nome'], row['descrição'], row.get('urgente', ''))


@then('a tarefa deve estar na pilha "{stack}"')
@then('as tarefas devem estar na pilha "{stack}"')
def check_task_on_stack(context, stack):
    """Checa os registros nas colunas corretas usando a tabela como base."""
    stack = {
        'A fazer': Todo,
        'Fazendo': Doing,
        'Pronto': Done,
    }[stack]
    stack_todos = stack(context.driver)
    tasks = stack_todos.get_tasks()

    table = [table_to_task(row) for row in context.table]

    assert check_stack(tasks, table)


@when('atualizar a página')
def reload_page(context):
    context.driver.refresh()


@then('a tarefa deve estar no topo da pilha "{stack}"')
def check_if_todo_is_first(context, stack):
    """
    Compara a primeiro todo da pilha `stack` com o todo da tabela.

    VARS:
        po_fist_task: todo do topo da stak
        todo_task: po_fist_task convertido para task (namedtuple)
        table_task: todo da tabela
    """
    todos = Todo(context.driver)
    po_fist_task = todos.get_tasks()[0]
    todo_task = task(po_fist_task.name, po_fist_task.desc, '')
    table_task = [table_to_task(row) for row in context.table][0]
    assert todo_task == table_task
