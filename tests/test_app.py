from flask import url_for
from app import create_app
"""
AAA

- Arrange - Arrumar o que é necessário
- Act - Agir, fazer o que queremos para o teste
- Assert - Garantir que o que foi feito deu certo
"""


def test_create_app():
    assert create_app()


def test_index_deve_retornar_42(client):
    # A - fixture
    response = client.get(url_for('home.index')) # A

    assert response.data.decode() == '42' # A


def test_index_deve_retornar_status_code_200(client):
    response = client.get(url_for('home.index'))

    assert response.status_code == 200


def test_api_todos_deve_retornar_uma_lista(client):
    response = client.get(url_for('api.todos'))

    assert isinstance(response.json, list)


def test_api_todos_deve_retornar_registros_de_todos(client):
    response = client.get(url_for('api.todos'))

    assert 'name' in response.json[0].keys()
    assert 'description' in response.json[0].keys()
