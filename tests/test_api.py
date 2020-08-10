from flask import url_for
from jsonschema import validate


def test_task_register_com_json_valido_deve_retonar_o_objeto_recebido(
    client, mocker
):
    data = {
        'name': 'Dormir',
        'description': 'Pq é bom',
        'state': 'todo',
        'urgent': False,
    }

    mocker.patch('app.api.current_app.db')
    request = client.post(url_for('api.task_register'), json=data)

    assert request.json == data
    assert request.status_code == 201


def test_task_register_com_json_vazio_deve_retonar_os_campos_faltantes(
    client,
):
    data = {}
    expected_keys = ['name', 'description', 'state', 'urgent']

    request = client.post(url_for('api.task_register'), json=data)

    assert request.status_code == 400
    assert all(map(lambda field: field in request.json.keys(), expected_keys))


def test_tasks_deve_retornar_um_grupo_de_tasks_validas(
    client, mocker, tasks, task_schema
):
    m = mocker.patch('app.api.Todo')
    m.query.all.return_value = tasks
    response = client.get(url_for('api.tasks'))

    assert validate(response.json, schema=task_schema) is None


# def test_change_task_state_deve_retornar_a_task_com_estado_alterado(
#     client, mocker, filtered_tasks
# ):
#     m = mocker.patch('app.api.Todo')
#     m.query.filter_by.first.return_value = filtered_tasks
#     data = ...
#     response = client.patch(
#         url_for('api.change_task_state', json=data)
#     )
#     assert False
