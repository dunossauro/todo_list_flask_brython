# Todo list

Exemplo de um projeto simples de TODO list usando flask + Brython

A ídeia principal do projeto é ser fullstack python, para fins demonstrativos


# Tarefas

## Front
- [x] Adicionar rota para mudar estado da task (Fazendo)
  - [ ] Mock da query no banco
  - [x] Serializer para receber o request
  - [x] Adicionar no front para redireciar os cards para coluna correta
- [ ] Adicionar prioridade nas tasks no front
- [ ] webcomponent para filtrar issues


## Views
- [ ] Criar view de login
  - [x] Criar o html
  - [x] Criar eventos de click
  - [ ] Inserir no template o erro do login
- [ ] Criar view de cadastro
  - [x] Criar rotas
  - [x] Criar o html
  - [x] Criar eventos de click
  - [ ] Inserir no template o erro do login
- [ ] Ajustar condições do Header
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
- [ ] Behave features
  - [ ] Login
  - [x] Cadastro
  - [x] Todo

## Ops
- [ ] Docker
- [ ] CI
- [ ] CD

## Outros
- [ ] Gunicorn
- [ ] Postgress
- [ ] Compose


## Brython issues
- [ ] Abrir issue no Brython (Não sabe ler url_for do jinja no --modules)
- [ ] Criar módulos do Brython (para minimizar os js)
