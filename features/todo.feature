# language: pt
Funcionalidade: Registrar tarefas

  Cenário: Registrar tarefa
    Dado que esteja na página de "todo"
    Quando registrar tarefa
      """
      {
          "nome": "Dormir",
          "description": "Pq é bom"
      }
      """
    Então a tarefa deve estar na pilha de "todo"
