from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, post_load
from .model import Todo

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



def configure(app):
    ma.init_app(app)
