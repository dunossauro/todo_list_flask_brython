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
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Carregamento automático das TODOS
    Quando registrar as tarefas
      | nome           | descrição             | urgente |
      | Liga para Beto | Telefone +15 51515151 | False   |
      | ir no mercado  | Promoção no mercado x | True    |
    E atualizar a página
    Então as tarefas devem estar na pilha de "todo"
      | nome           | descrição             |
      | Liga para Beto | Telefone +15 51515151 |
      | ir no mercado  | Promoção no mercado x |
    E a tarefa deve estar no topo da pilha de "todo"
      | nome           | descrição             |
      | ir no mercado  | Promoção no mercado x |

  Cenário: Prioridades de tarefas
      Quando registrar as tarefas
        | nome           | descrição               | urgente |
        | Fazer bolo     | não esquecer o fermento | False   |
        | ir no mercado  | Promoção no mercado x   | True    |

      Então a tarefa deve estar no topo da pilha de "todo"
        | nome           | descrição             |
        | ir no mercado  | Promoção no mercado x |
