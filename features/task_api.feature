# language: pt

@api
Funcionalidade: API de tarefas
  Cenário: Registrar uma tarefa
  """
  /tasks <- POST para registrar uma nova tarefa
  /tasks/id <- GET para ver se a tarefa foi inserida
  """
    Quando criar uma nova tarefa via API
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Então a tarefa deve ter sido criada
