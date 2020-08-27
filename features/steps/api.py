from behave import when, then
from httpx import get, post

# TODO: Criar usuário antes de executar esses steps

@when('criar uma nova tarefa via API')
@when('criar novas tarefas via API')
def create_task_using_api(context):
    for row in context.table:
        json = {
            'name': row['nome'],
            'description': row['descrição'],
            'urgent': row.get('urgente', False),
            'state': 'todo',
            'user_id': 1,
        }
        req = post(context.base_url + 'tasks', json=json).status_code
        assert req == 201


@then('a tarefa deve ter sido criada')
def check_created_task(context):
    ...
