from flask import url_for


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


def test_login_deve_retornar_o_template_de_login(client):
    request = client.get(url_for("front.login"))
    assert "Login" in request.data.decode()
