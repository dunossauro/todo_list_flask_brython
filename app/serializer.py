from flask_login import current_user
from flask_marshmallow import Marshmallow
from marshmallow import fields, post_load

from .model import Todo, User

ma = Marshmallow()


class TodoSchema(ma.SQLAlchemyAutoSchema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    urgent = fields.Boolean(required=True)
    state = fields.String(required=True)

    @post_load
    def make_todo(self, data, **kwargs):
        return Todo(user_id=current_user.id, **data)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


def configure(app):
    ma.init_app(app)
