from flask import Blueprint, render_template


front = Blueprint('front', __name__)


@front.route('/todo', methods=['GET'])
def todo():
    return render_template('todo.html')
