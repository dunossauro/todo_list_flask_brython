from random import choice

from app import create_app
from app.model import Todo
from factory import Factory, Faker, Sequence
from faker.providers import BaseProvider
from pytest import fixture


class TaksProvider(BaseProvider):
    def todo_state(self):
        return choice(['todo', 'doing', 'done'])


Faker.add_provider(TaksProvider)

schema = {
    "type": "array",
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'description': {'type': 'string'},
        'urgent': {'type': 'boolean'},
        'state': {'type': 'string'},
    },
}


class TodoFactory(Factory):
    class Meta:
        model = Todo

    id = Sequence(lambda n: n)
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
    yield client
    app_context.pop()


@fixture(scope='function')
def tasks():
    return TodoFactory.build_batch(5)


@fixture(scope='function')
def filtered_tasks():
    return TodoFactory()


@fixture(scope='function')
def task_schema():
    return schema
