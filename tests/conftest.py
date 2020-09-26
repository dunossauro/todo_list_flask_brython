from random import choice

from factory import Factory, Faker, Sequence
from faker.providers import BaseProvider
from flask import template_rendered
from pytest import fixture

from app import create_app
from app.model import Todo, User


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
def db(app):
    with app.app_context():
        app.db.create_all()

        yield app.db

        app.db.session.remove()
        app.db.drop_all()


@fixture
def client(app, db):
    with app.test_client() as client:
        app.db.session.add(
            User(name='test', password='test', email='test@test')
        )
        yield client


@fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_context = app.test_request_context()
    app_context.push()

    return app


@fixture
def templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append(template)

    template_rendered.connect(record, app)

    yield recorded

    template_rendered.disconnect(record, app)


@fixture(scope='function')
def tasks():
    return TodoFactory.build_batch(5)


@fixture(scope='function')
def filtered_tasks():
    return TodoFactory()


@fixture(scope='function')
def task_schema():
    return schema
