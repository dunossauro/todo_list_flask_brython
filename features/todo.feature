# language: pt
Funcionalidade: Registrar tarefas
  Contexto: Login
    Dado que esteja logado
    E que esteja na página de "todo"

  Cenário: Registrar tarefa
    Quando registrar tarefa
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Então a tarefa deve estar na pilha de "todo"
