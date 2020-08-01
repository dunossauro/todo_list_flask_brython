from browser import html, document, ajax, bind
from javascript import JSON


def request(url, json, method='POST'):
    """Send json data to backend."""
    req = ajax.Ajax()
    req.bind('complete', create_todo_div)
    req.open(method, url, True)
    req.set_header('content-type', 'application/json')
    req.send(JSON.stringify(json))
    return req


def create_todo_div(req):
    json = JSON.parse(req.text)
    for todo in json:
        div = html.DIV(Class='terminal-card')
        div <= html.HEADER(f'{todo["name"]}')
        div <= html.DIV(f'Descrição: {todo["description"]}')
        buts = html.DIV(Class='buttons')
        buts <= html.BUTTON('Fazer!', Class='btn btn-primary btn-ghost')
        buts <= html.BUTTON('Cancelar!', Class='btn btn-error btn-ghost')
        div <= buts
        document.select_one('div.todo div.terminal-timeline') <= div


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


ajax.get('/todos', oncomplete=create_todo_div)
