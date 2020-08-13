from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_login import login_user, login_required, logout_user
from .model import User


front = Blueprint('front', __name__)


@front.route('/', methods=['GET'])
@login_required
def todo():
    return render_template('todo.html')


@front.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@front.route('/login', methods=['POST'])
def login_post():
    user = User().login(
        request.form.get('email', ''), request.form.get('senha', '')
    )
    if user:
        login_user(user)
        return redirect('/')

    return redirect(url_for('front.login'))


@front.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('.login'))
