from flask import Blueprint, render_template, request, current_app, redirect
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
    login_data = request.form

    login_data.get('senha', '')
    user = User().login(
        login_data.get('email', ''),
        login_data.get('senha', '')
    )
    if user:
        login_user(user)
        return redirect('/')
    return redirect('/')


@front.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/')
