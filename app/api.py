from flask import Blueprint, jsonify, request, current_app
from marshmallow import ValidationError
from .serializer import TodoSchema
from .model import Todo

api = Blueprint('api', __name__)


@api.route('/tasks', methods=['GET'])
def tasks():
    ts = TodoSchema(many=True)
    query_result = Todo.query.all()
    return jsonify(ts.dump(query_result)), 200


@api.route('/task-register', methods=['POST'])
def task_register():
    ts = TodoSchema()
    try:
        task = ts.load(request.json)
        current_app.db.session.add(task)
        current_app.db.session.commit()
        return ts.dump(task), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
