from flask import url_for
from app.model import Todo


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


def test_task_register_com_json_vazio_deve_retonar_o_os_campos_faltantes(
    client,
):
    data = {}
    expected_keys = ['name', 'description', 'state', 'urgent']

    request = client.post(url_for('api.task_register'), json=data)

    assert request.status_code == 400
    assert all(map(lambda field: field in request.json.keys(), expected_keys))


def test_tasks_deve_retornar_um_grupo_de_tasks(client):
    ...
