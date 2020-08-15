from json import loads

from behave import given, then, when
from features.modules.todo import check_stack, table_to_task
from features.page_objects.pages import CreateTodo, Todo


@given('que esteja na página de "{page}"')
def natigate_to_page(context, page):
    pages = {'todo': '', 'register': 'register'}
    context.driver.get(context.base_url + pages[page])


@when('registrar tarefa')
@when('registrar as tarefas')
def task_register(context):
    """
    Registra uma ou mais tarefas usando a tabela do Gherking.

    TODO: Melhorar tempo desse teste, antes do request ser feito
        Os dados são preenchidos novamente, enviando as vezes
        somente um registro (com todos da tabela) #7
    """
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
    """
    Checa os registros nas colunas corretas usando a tabela como base.

    #TODO: Os testes que checam os registros inseridos no banco de
        dados estavam fazendo uma asserção simples.
        A função foi refatorada mais ainda não exibe os resultados
        reais nos steps de validação #8
    """
    todos = Todo(context.driver)
    tasks = todos.get_tasks()

    table = [table_to_task(row) for row in context.table]

    assert check_stack(tasks, table)


@when('atualizar a página')
def reload_page(context):
    context.driver.refresh()
