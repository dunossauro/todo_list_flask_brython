from flask import Blueprint

home = Blueprint('home', __name__)


@home.route('/index', methods=['GET'])
def index():
    return '42', 200
