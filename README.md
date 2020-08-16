# Todo list

Exemplo de um projeto simples de TODO list usando flask + Brython

A ideia principal do projeto é ser fullstack python, para fins demonstrativos


# Tarefas

## Front
- [x] Adicionar rota para mudar estado da task (Fazendo)
  - [ ] Mock da query no banco
  - [x] Serializer para receber o request
  - [x] Adicionar no front para redireciar os cards para coluna correta
- [x] Adicionar prioridade nas tasks no front
- [ ] Webcomponent para filtrar issues
- [ ] Criar widget para editar todos quando clicar no todo


## API
- [ ] Criar patch para editar conteúdo dos todos

## Views
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


## Login/Admin
- [x] Criar models de usuários
- [x] Integração com flask login
- [ ] Integração com flask admin


## Testes de Integração
- [x] Page objects
  - [x] Login
  - [x] Cadastro
  - [x] Todo
- [x] Behave features
  - [x] Login
  - [x] Cadastro
  - [x] Todo
- [x] Movimentação dos cartões

## Ops
- [ ] Docker
- [ ] CI
  - [x] Code style
  - [ ] Testes de unidade
  - [ ] Testes E2E
- [ ] CD - Heroku

## Outros
- [ ] Gunicorn
- [ ] Postgres
- [ ] Compose
- [ ] Logs


## Brython issues
- [ ] Abrir issue no Brython (Não sabe ler url_for do jinja no --modules)
- [ ] Criar módulos do Brython (para minimizar os js)
