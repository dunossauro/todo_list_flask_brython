from functools import partial

from browser import ajax, bind, document, html
from javascript import JSON


def card_elements(event):
    card = event.target.parentNode.parentNode
    error = card.select_one('.btn-error')
    primary = card.select_one('.btn-primary')
    task_id = card.select_one('header').text.split('#')[1]
    return card, primary, error, task_id


def do(evt):
    card, primary, error, task_id = card_elements(evt)

    # Texto
    primary.text = 'Pronto!'
    error.text = 'Voltar'

    # Unbinding
    primary.unbind('click', do)
    error.unbind('click', cancel)

    # binds
    primary.bind('click', done)
    error.bind('click', back)
    change_state(task_id, 'doing')
    document.select_one('div.doing div.terminal-timeline') <= card


def cancel(evt):
    card, primary, error, task_id = card_elements(evt)
    change_state(task_id, 'canceled')
    card.remove()


def done(evt):
    card, primary, error, task_id = card_elements(evt)
    primary.text = 'Refazer!'
    error.remove()
    primary.unbind('click', done)
    primary.bind('click', redo)

    change_state(task_id, 'done')

    document.select_one('div.done div.terminal-timeline') <= card


def back(evt):
    card, primary, error, task_id = card_elements(evt)
    # Texto
    primary.text = 'Fazer!'
    error.text = 'Cancelar!'

    # Unbinding
    primary.unbind('click', done)
    error.unbind('click', back)

    # binds
    primary.bind('click', do)
    error.bind('click', cancel)
    change_state(task_id, 'todo')
    document.select_one('div.todo div.terminal-timeline') <= card


def redo(evt):
    card, primary, error, task_id = card_elements(evt)
    internal_div = card.select('div')[1]

    primary.text = 'Fazer!'
    primary.unbind('click', redo)
    primary.bind('click', do)

    error = html.BUTTON('Cancelar!', Class='btn btn-error btn-ghost cancel')

    error.bind('click', cancel)

    internal_div <= error
    change_state(task_id, 'todo')
    document.select_one('div.todo div.terminal-timeline') <= card


def html_card(todo, do_action, cancel_action=None):
    """
    Gera um card html usando o todo como referência.

    Args:
        - todo: {'name': 'name', 'id': 'id', 'description': 'description'}
        - do_action: {'text': 'Fazer!', 'action': bind}
        - cancel_action: {'text': 'Cancelar!', 'action': bind}
    Note:
        *_acions = Dict[str, Union[str, Callable]]
    """
    div = html.DIV(Class='terminal-card')
    div <= html.HEADER(f'{todo["name"]} #{todo["id"]}')
    div <= html.DIV(f'Descrição: {todo["description"]}')
    buts = html.DIV(Class='buttons')

    do_button = html.BUTTON(
        do_action['text'], Class='btn btn-primary btn-ghost do'
    )
    buts <= do_button
    do_button.bind('click', do_action['action'])

    if cancel_action:
        cancel_button = html.BUTTON(
            cancel_action['text'], Class='btn btn-error btn-ghost cancel'
        )
        cancel_button.bind('click', cancel_action['action'])
        buts <= cancel_button

    div <= buts

    return div


html_todo = partial(
    html_card,
    do_action={'text': 'Fazer!', 'action': do},
    cancel_action={'text': 'Cancelar!', 'action': cancel},
)

html_doing = partial(
    html_card,
    do_action={'text': 'Pronto!', 'action': done},
    cancel_action={'text': 'Voltar!', 'action': back},
)

html_done = partial(html_card, do_action={'text': 'Refazer!', 'action': redo})


def change_state(task_id, new_state):
    req = ajax.Ajax()
    req.open('PATCH', f'/change-state/{task_id}/{new_state}', True)
    req.set_header('content-type', 'application/json')
    req.send()


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
    request('/task-register', json=json, bind=register_task)

    name.value = ''
    desc.value = ''


def request(url, json, bind, method='POST'):
    """Send json data to backend."""
    req = ajax.Ajax()
    req.bind('complete', bind)
    req.open(method, url, True)
    req.set_header('content-type', 'application/json')
    req.send(JSON.stringify(json))
    return req


def register_task(req):
    json_response = JSON.parse(req.text)
    document.select_one('div.todo div.terminal-timeline') <= html_todo(
        json_response
    )


def get_todos(req):
    todo_states = {'todo': html_todo, 'doing': html_doing, 'done': html_done}
    json = JSON.parse(req.text)
    for todo in json:
        div = document.select_one(f'div.{todo["state"]} div.terminal-timeline')
        div <= todo_states[todo['state']](todo)


ajax.get('/tasks', oncomplete=get_todos)
