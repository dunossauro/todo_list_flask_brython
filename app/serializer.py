from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from .model import Todo

ma = Marshmallow()


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True
        fields = ('name', 'state', 'description', 'urgent')

    name = fields.String(required=True)
    description = fields.String(required=True)
    urgent = fields.Boolean(required=True)
    state = fields.String(required=True)


def configure(app):
    ma.init_app(app)
