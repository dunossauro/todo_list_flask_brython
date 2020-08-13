from browser import bind, document


@bind('input[name="nome"]', 'focus')
def xpto(evnt):
    document.select_one(
        'label[for="nome"]'
    ).text = 'Lembre-se de colocar um falso'


@bind('input[name="nome"]', 'blur')
def xpto(evnt):
    document.select_one('label[for="nome"]').text = 'Nome:'


@bind('input[name="senha"]', 'focus')
def xpto(evnt):
    document.select_one('label[for="senha"]').text = 'Será que é segura?'


@bind('input[name="senha"]', 'blur')
def xpto(evnt):
    document.select_one('label[for="senha"]').text = 'Senha:'


@bind('input[name="email"]', 'focus')
def xpto(evnt):
    document.select_one(
        'label[for="email"]'
    ).text = 'Se for válido, todo mundo vai saber'


@bind('input[name="email"]', 'blur')
def xpto(evnt):
    document.select_one('label[for="email"]').text = 'Email:'
