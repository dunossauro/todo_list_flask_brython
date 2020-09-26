from flask import url_for
from .conftest import login


def test_todo_deve_renderizar_a_view_de_login_quando_nao_estiver_logado(
    client, templates
):
    response = client.get(url_for('front.todo'), follow_redirects=True)

    assert templates[0].name == 'login.html'


def test_todo_deve_renderizar_a_view_de_todo_quando_estiver_logado(
    client, templates
):
    login(client)

    response = client.get(url_for('front.todo'), follow_redirects=True)

    assert templates[0].name == 'todo.html'


def test_register_deve_retonar_pagina_de_registro(client):
    request = client.get(url_for("front.register"))
    assert "Cadastro" in request.data.decode()


def test_resgiter_post_com_dados_válidos_deve_invocar_login_user(
    client, mocker
):
    mocked = mocker.patch("app.front.login_user")
    request = client.post(
        url_for("front.register_post"),
        data=dict(nome="test", senha="test", email="test@test.test"),
    )
    assert mocked.called
    assert request.status_code == 302


def test_register_post_com_dados_inválidos_deve_retonar_pagina_inicial_com_erro(  # NOQA
    client,
):
    request = client.post(
        url_for("front.register_post"), data=dict(nome="test")
    )
    assert "Algo deu errado" in request.data.decode()
    assert request.status_code == 200


def test_login_deve_retornar_o_template_de_login(client, templates):
    client.get(url_for('front.login'))
    assert templates[0].name == 'login.html'


def test_login_deve_redicionar_para_view_de_login_com_dados_inválidos(
    client, templates
):
    login(client, email='batatinha@batata')
    assert templates[0].name == 'login.html'


def test_logout_deve_renderizar_o_template_de_login(client, templates):
    login(client)
    client.post(url_for('front.logout'), follow_redirects=True)
    assert templates[1].name == 'login.html'


def test_logout_deve_ser_redirecionado_para_rota_de_login(client):
    login(client)
    response = client.post(url_for('front.logout'))
    assert '/login' in response.location
