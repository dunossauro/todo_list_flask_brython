# Executando o projeto

O projeto todo foi concebido usando python 3.8.5. O projeto deve funcionar para qualquer versão do python 3.8, porém algumas features pode não funcionar corretamente com versões menores ou maiores. Você pode usar o pyenv para gerenciar as instalações de versões do python. Se você já usa pyenv, temos um arquivo `.python-version` no projeto e isso não deve ser um problema para você.

> Projeto atualizado para 3.9.2 (02/04/2021)

## Configurando o poetry

O projeto todo é usado com base no [Poetry](https://python-poetry.org/). Tanto o gerenciamento de ambiente virtual, quanto as instalações de pacotes. Certifique-se que você tem o poetry instalado no seu ambiente, caso não tenha:

```bash
pip install poetry  # pip3 caso ainda tenha o python 2 instalado
poetry install      # Para instalar todos os pacotes
poetry shell        # Para reproduzir os comando a seguir nesse documento
```

Lembrando que caso não gostei de usar `poetry shell` você pode usar `poetry run` antes de cada linha desse tutorial, como por exemplo `poetry run flask db update`


## Como rodar a aplicação em desenvolvimento?

Antes de tudo é necessário declarar as variáveis de ambiente do Flask.

Caso você deseje rodar os testes de comportamento, eles fazem uso de rotas exclusivas que são executadas somente no `FLASK_ENV=testing`

```bash
export FLASK_APP=app

export FLASK_ENV=development

```

Caso queira rodar os ambientes de desenvolvimento e testes com banco de dados PostgreSQL execute:

```bash
docker-compose -f docker-compose-database.yml up -d

export DATABASE_URL=postgresql://user_root:user_pass_123@localhost/todolist_db

```

(credenciais de acesso ao banco contidas no arquivo `docker-compose-database.yml`)

Lembrando que é importante que você rode as migrações para que o banco esteja configurado.

```bash
flask db upgrade
```

Aí sim podemos rodar nosso projeto

```bash
flask run
```

Assim a aplicação deve ser iniciada sem grandes problemas.


Também foi criado um [script](./start.sh) que sobe a aplicação com um único comando

```bash
bash start.sh
```
---

## Executando com docker

```bash
docker build -f dockerfile-app . -t todo_list

docker run -it -p 80:80 --name="todo_list" todo_list
```

## Executando o docker-compose

```bash
docker-compose up --build
```

# Rodando os testes de unidade

Caso tenha interesse em rodar os testes de unidade, você deve se certificar que está com as variáveis de ambiente do flask configuradas.

```bash
python -m pytest  # Ou somente pytest, após um `pip install -e.`
```

Caso você queira ver a cobertura dos testes
```bash
coverage --source app -m pytest
```

Ver o report de cobertura

```bash
coverage html
```

Os arquivos serão gerados na pasta 'htmlcov'. Você pode abrir o `index.html` no seu browser de preferência e explorar o que não está coberto.
