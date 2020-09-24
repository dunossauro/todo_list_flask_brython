# language: pt
Funcionalidade: Criação de tarefas
  Contexto: Entrar na área logada
    Dado que esteja logado
    E que esteja na página de "todo"

  Cenário: Criar tarefa
    Quando criar tarefa
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Então a tarefa deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Carregamento automático das TODOS
    Quando criar as tarefas
      | nome           | descrição             | urgente |
      | Liga para Beto | Telefone +15 51515151 | False   |
      | ir no mercado  | Promoção no mercado x | True    |
    E atualizar a página
    Então as tarefas devem estar na pilha "A fazer"
      | nome           | descrição             |
      | Liga para Beto | Telefone +15 51515151 |
      | ir no mercado  | Promoção no mercado x |
    E a tarefa deve estar no topo da pilha "A fazer"
      | nome           | descrição             |
      | ir no mercado  | Promoção no mercado x |

  Cenário: Prioridades de tarefas
      Quando criar as tarefas
        | nome           | descrição               | urgente |
        | Fazer bolo     | não esquecer o fermento | False   |
        | ir no mercado  | Promoção no mercado x   | True    |

      Então a tarefa deve estar no topo da pilha "A fazer"
        | nome           | descrição             |
        | ir no mercado  | Promoção no mercado x |

  Cenário: Não deve ser possível criar uma tarefa com nome vazio
     Quando criar uma tarefa sem nome
     Então a mensagem de erro deverá ser exibida
      """
      Você esqueceu de preencher o campo "Nome"
      """

  Cenário: Tarefa urgente deve exibir indicador de urgência
    Quando criar tarefa
      | nome       | descrição               | urgente |
      | Fazer bolo | não esquecer o fermento | True    |
    Então a tarefa no topo da pilha "A fazer" deverá ter indicativo de urgência

  Cenário: Tarefa sem urgência não deve exibir indicador de urgência
    Quando criar tarefa
      | nome       | descrição               | urgente |
      | Fazer bolo | não esquecer o fermento | False   |
    Então a tarefa no topo da pilha "A fazer" não deverá ter indicativo de urgência

  Cenário: Não deve ser possível criar uma tarefa com mais de 80 caracteres no campo nome
    Quando criar tarefa com 81 ou mais caracteres no campo nome
    Então a mensagem de aviso deverá ser exibida
      """
      Ei, o campo "Nome" da sua tarefa está muito grande, o limite é 80 caracteres
      """

  Cenário: Não deve ser possível criar uma tarefa com mais de 300 caracteres na descrição
    Quando criar tarefa com 301 ou mais caracteres no campo descrição
    Então a mensagem de aviso deverá ser exibida
      """
      Ei, o campo "Descrição" da sua tarefa está muito grande, o limite é 300 caracteres
      """
