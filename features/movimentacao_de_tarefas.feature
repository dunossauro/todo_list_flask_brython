# language: pt
Funcionalidade: Movimentação de tarefas
  Contexto: Entrar na área logada e registrar tarefas
    Dado que esteja logado
    E que esteja na página de "todo"
    E que as tarefas estejam criadas
      | nome    | descrição         |
      | Dormir  | Pq é bom          |
      | Acordar | Pois é necessário |
      | Comer   | Se não eu morro   |

  Cenário: Mover tarefa para Fazendo
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    E as tarefas devem estar na pilha "A fazer"
      | nome    | descrição |
      | Acordar | Pois é necessário |
      | Comer   | Se não eu morro   |

  Cenário: Mover tarefa para Pronto
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Quando concluir a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Pronto"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Voltar cartão para A fazer
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Quando voltar a tarefa "Dormir"
    Então a tarefa deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Cancelar cartão
    Quando cancelar a tarefa "Dormir"
    Então a tarefa não deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Quando atualizar a página
    Então a tarefa não deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Cartões devem ser carregados nas colunas corretas
    Quando fazer a tarefa "Dormir"
    E concluir a tarefa "Dormir"
    E fazer a tarefa "Acordar"
    E atualizar a página
    Então a tarefa deve estar na pilha "Fazendo"
      | nome    | descrição         |
      | Acordar | Pois é necessário |
    E a tarefa deve estar na pilha "Pronto"
      | nome   | descrição |
      | Dormir | Pq é bom  |
