from flask import Blueprint, jsonify, request, current_app
from marshmallow import ValidationError
from .serializer import UserSchema
from .model import Todo

api = Blueprint('api', __name__)


@api.route('/tasks', methods=['GET'])
def todos():
    ...

@api.route('/task-register', methods=['POST'])
def task_register():
    us = UserSchema()
    try:
        task = us.load(request.json)
        current_app.db.session.add(task)
        current_app.db.session.commit()
        return us.dump(task), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
