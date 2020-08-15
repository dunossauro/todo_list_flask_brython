# language: pt
Funcionalidade: Registrar usuários

  Cenário: A aplicação deve redirecionar para a página de TODO ao registrar um usuário com sucesso
    Dado que esteja na página de "register"
    Quando registrar o usuário
      """
      {
          "nome": "Beto Cone",
          "email": "beto@cone.com",
          "senha": "123"
      }
      """
    Então deverá ser redirecionado para a pagina de "todo"

  Cenário: A aplicação deve redirecionar para a página de register ao tentar cadastrar um usuário com e-mail já cadastrado
    Dado que esteja na página de "register"
    Quando registrar o usuário
      """
      {
          "nome": "Beto Cone",
          "email": "beto@cone.com",
          "senha": "123"
      }
      """
    Dado faça logout
    E que esteja na página de "register"
    Quando registrar o usuário
      """
      {
          "nome": "Beto Cone",
          "email": "beto@cone.com",
          "senha": "123"
      }
      """
    Então a mensagem de erro deverá ser exibida
      """
      Algo deu errado!
      """

  Cenário: A aplicação deve alterar o label do Email quando inserido um Email inválido
    Dado que esteja na página de "register"
    Quando registrar o usuário
      """
      {
          "nome": "Beto Cone",
          "email": "beto",
          "senha": "123"
      }
      """
    Então o label do Email deverá ser "Se for válido, todo mundo vai saber"
