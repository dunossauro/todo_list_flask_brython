from jsonschema import validate

from flask import url_for

from .conftest import login


def test_task_register_com_json_valido_deve_retonar_o_objeto_recebido(client):
    login(client)
    data = {
        'name': 'Dormir',
        'description': 'Pq é bom',
        'state': 'todo',
        'urgent': False,
    }

    request = client.post(url_for('api.task_register'), json=data)

    del request.json['id']

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


# def test_change_task_state_deve_retornar_a_task_com_estado_alterado(client):
#     login(client)
#
#     response = client.patch(
#         url_for('api.change_task_state', json=data)
#     )
#     assert False
