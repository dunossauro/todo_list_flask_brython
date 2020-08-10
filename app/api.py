from flask import Blueprint, jsonify, request, current_app
from marshmallow import ValidationError
from .serializer import TodoSchema
from .model import Todo

api = Blueprint('api', __name__)


@api.route('/tasks', methods=['GET'])
def tasks():
    ts = TodoSchema(many=True)
    query_result = Todo.query.filter(Todo.state != 'canceled').all()
    return jsonify(ts.dump(query_result)), 200


@api.route('/change-state/<int:_id>/<new_state>', methods=['PATCH'])
def change_task_state(_id, new_state):
    ts = TodoSchema()
    states = ['todo', 'doing', 'done', 'canceled']

    task = Todo.query.filter_by(id=_id).one()

    if new_state in states:
        task.state = new_state
        current_app.db.session.commit()

    return jsonify(ts.dump(task))


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
