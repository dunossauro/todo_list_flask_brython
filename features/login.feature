# language: pt
Funcionalidade: Login
  Contexto: Oágina de login
    Dado que esteja na página de "login"

  Cenário: Login com credenciais inválidas
    Quando logar com credenciais inválidas
    Então a mensagem de erro deverá ser exibida
      """
      Email ou senha inválidos!
      """

  @criar_usuario
  Cenário: Login com credenciais válidas
    Quando logar com credenciais válidas
    Então deverá ser redirecionado para a pagina de "todo"
