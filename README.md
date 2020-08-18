# Full-stack python

Projeto de exemplo usando fullstack python.

O projeto tem a intensão de ser um todo-list integrado a um kanban simples para exercitar as chamadas de ajax.


O back-end do projeto foi contruído usando flask, um microframework e o front-end foi desenvolvido usando [Brython](http://brython.info).

Os testes de unidade foram feitos usando pytest e os testes E2E rodam sob Behave (Behavior-Driven-Development), nos quais foram pensadas as especificações por exemplo, durante as lives no twitch.


## Tarefas a serem feitas

### Front
- [x] Adicionar rota para mudar estado da task (Fazendo)
  - [ ] Mock da query no banco
  - [x] Serializer para receber o request
  - [x] Adicionar no front para redireciar os cards para coluna correta
- [x] Adicionar prioridade nas tasks no front
- [ ] Webcomponent para filtrar issues
- [ ] Criar widget para editar todos quando clicar no todo


### API
- [ ] Criar patch para editar conteúdo dos todos

### Views
- [x] Criar view de login
  - [x] Criar o html
  - [x] Criar eventos de click
  - [x] Inserir no template o erro do login
- [x] Criar view de cadastro
  - [x] Criar rotas
  - [x] Criar o html
  - [x] Criar eventos de click
  - [x] Inserir no template o erro da criação
- [x] Ajustar CSS do Header
- [x] Ajustar condições do Header
- [ ] Criar Footer


### Login/Admin
- [x] Criar models de usuários
- [x] Integração com flask login
- [ ] Integração com flask admin


### Testes de Integração
- [x] Page objects
  - [x] Login
  - [x] Cadastro
  - [x] Todo
- [x] Behave features
  - [x] Login
  - [x] Cadastro
  - [x] Todo
- [x] Movimentação dos cartões

### Ops
- [ ] Docker
- [ ] CI
  - [x] Code style
  - [ ] Testes de unidade
  - [ ] Testes E2E
- [ ] CD - Heroku

### Outros
- [ ] Gunicorn
- [ ] Postgres
- [ ] Compose
- [ ] Logs


### Brython issues
- [ ] Abrir issue no Brython (Não sabe ler url_for do jinja no --modules)
- [ ] Criar módulos do Brython (para minimizar os js)


## Como rodar a aplicação

### Modo de desenvolvimento:
Antes de tudo é necessário declarar as variavéis de ambiente do Flask
```
export FLASK_APP=app

export FLASK_ENV=development
```
Agora vamos rodar as migrações do banco
```
flask db upgrade
```
Então podemos subir a aplicação
```
flask run
```

### Executando o Dockerfile
```
docker build -f dockerfile-app . -t todo_list

docker run -it -p 80:80 --name="todo_list" todo_list
```

### Executando o docker-compose
```
docker-compose up --build
```
