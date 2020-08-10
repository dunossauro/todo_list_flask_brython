export FLASK_APP=app
export FLASK_DEBUG=True

flask db upgrade
flask run
