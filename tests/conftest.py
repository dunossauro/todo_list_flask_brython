from random import choice
from pytest import fixture
from app import create_app
from factory import Faker, Factory
from app.model import Todo
from faker.providers import BaseProvider


class TaksProvider(BaseProvider):
    def todo_state(self):
        return choice(['todo', 'doing', 'done'])


Faker.add_provider(TaksProvider)

schema = {
    "type": "array",
    'properties': {
        'name': {'type': 'string'},
        'description': {'type': 'string'},
        'urgent': {'type': 'boolean'},
        'state': {'type': 'string'},
    }
}

class TodoFactory(Factory):
    class Meta:
        model = Todo

    name = Faker('sentence', nb_words=4)
    description = Faker('sentence', nb_words=4)
    urgent = Faker('boolean')
    state = Faker('todo_state')


@fixture
def client():
    app = create_app()
    app_context = app.test_request_context()
    app_context.push()
    client = app.test_client()

    # ------------------- Antes do teste ^

    yield client  # ------------- Vai ser passado para o teste

    # ------------- O que vai acontecer depois do teste V
    app_context.pop()


@fixture(scope='function')
def tasks():
    return lambda: TodoFactory.build_batch(5)


@fixture(scope='function')
def task_schema():
    return schema
