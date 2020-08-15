from flask import Blueprint, current_app, jsonify, request
from marshmallow import ValidationError

from .model import Todo, User
from .serializer import UserSchema

tests = Blueprint('tests', __name__)


@tests.route('/remove-users', methods=['GET'])
def remove_all_users():
    User.query.delete()
    current_app.db.session.commit()
    return 'All users removed', 200


@tests.route('/remove-todos', methods=['GET'])
def remove_all_tasks():
    Todo.query.delete()
    current_app.db.session.commit()
    return 'All todos removed', 200


@tests.route('/register-users', methods=['POST'])
def register_new_user():
    us = UserSchema()
    try:
        user = us.load(request.json)
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return us.dump(user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
