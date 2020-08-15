# language: pt
Funcionalidade: Criação de conta

  Cenário: A aplicação deve redirecionar para a página de TODO ao registrar um usuário com sucesso
    Dado que esteja na página de "register"
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Então deverá ser redirecionado para a pagina de "todo"

  Cenário: A aplicação deve redirecionar para a página de register ao tentar cadastrar um usuário com e-mail já cadastrado
    Dado que esteja na página de "register"
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Dado faça logout
    E que esteja na página de "register"
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Então a mensagem de erro deverá ser exibida
      """
      Algo deu errado!
      """
