from browser import html, document, ajax, bind
from javascript import JSON


def card_elements(event):
    card = event.target.parentNode.parentNode
    error = card.select_one('.btn-error')
    primary = card.select_one('.btn-primary')
    return card, primary, error


def do(evt):
    card, primary, error = card_elements(evt)

    # Texto
    primary.text = 'Pronto!'
    error.text = 'Voltar'

    # Unbinding
    primary.unbind('click', do)
    error.unbind('click', cancel)

    # binds
    primary.bind('click', done)
    error.bind('click', back)

    document.select_one('div.doing div.terminal-timeline') <= card


def cancel(evt):
    card, primary, error = card_elements(evt)
    card.remove()


def done(evt):
    card, primary, error = card_elements(evt)
    primary.text = 'Refazer!'
    error.remove()
    primary.unbind('click', done)
    primary.bind('click', redo)

    document.select_one('div.done div.terminal-timeline') <= card


def back(evt):
    card, primary, error = card_elements(evt)
    # Texto
    primary.text = 'Fazer!'
    error.text = 'Cancelar!'

    # Unbinding
    primary.unbind('click', done)
    error.unbind('click', back)

    # binds
    primary.bind('click', do)
    error.bind('click', cancel)

    document.select_one('div.todo div.terminal-timeline') <= card


def redo(evt):
    card, primary, error = card_elements(evt)
    internal_div = card.select('div')[1]

    primary.text = 'Fazer!'
    primary.unbind('click', redo)
    primary.bind('click', do)

    error = html.BUTTON('Cancelar!', Class='btn btn-error btn-ghost cancel')

    error.bind('click', cancel)

    internal_div <= error

    document.select_one('div.todo div.terminal-timeline') <= card


def request(url, json, method='POST'):
    """Send json data to backend."""
    req = ajax.Ajax()
    req.bind('complete', create_card)
    req.open(method, url, True)
    req.set_header('content-type', 'application/json')
    req.send(JSON.stringify(json))
    return req


def create_card(todo):
    div = html.DIV(Class='terminal-card')
    div <= html.HEADER(f'{todo["name"]} #{todo["id"]}')
    div <= html.DIV(f'Descrição: {todo["description"]}')
    buts = html.DIV(Class='buttons')

    do_button = html.BUTTON('Fazer!', Class='btn btn-primary btn-ghost do')
    do_button.bind('click', do)

    cancel_button = html.BUTTON(
        'Cancelar!', Class='btn btn-error btn-ghost cancel'
    )
    cancel_button.bind('click', cancel)

    buts <= do_button
    buts <= cancel_button
    div <= buts
    document.select_one('div.todo div.terminal-timeline') <= div


def get_todos(req):
    json = JSON.parse(req.text)
    for todo in json:
        create_card(todo)


@bind('#submit', 'click')
def task_register(evt):
    name = document.select_one('[name="name"]')
    desc = document.select_one('[name="desc"]')
    urgent = document.select_one('[name="urgent"]')

    json = {
        'name': name.value,
        'description': desc.value,
        'urgent': urgent.checked,
        'state': 'todo',
    }

    request('/task-register', json=json)


ajax.get('/tasks', oncomplete=get_todos)
