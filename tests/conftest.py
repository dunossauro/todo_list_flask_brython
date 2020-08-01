from pytest import fixture
from app import create_app
from factory import Factory, Faker
from app.models import Todo


class TodoFactory(Factory):
    class Meta:
        model = Todo

    name = Faker('sentence', nb_words=4)
    description = Faker('sentence', nb_words=4)
    urgent = Faker('boolean')


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
    ...
