from browser import bind, document


@bind('[name="email"]', 'focus')
def email_click(evt):
    document.select_one('label[for="email"]').text = 'Tá certo?'


@bind('[name="email"]', 'blur')
def email_click(evt):
    document.select_one('label[for="email"]').text = 'Email:'


@bind('[name="senha"]', 'focus')
def email_click(evt):
    document.select_one('label[for="senha"]').text = 'Não vai errar'


@bind('[name="senha"]', 'blur')
def email_click(evt):
    document.select_one('label[for="senha"]').text = 'Senha:'
