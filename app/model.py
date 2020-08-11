from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin


db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def login(self, user, password):
        user = self.query.filter_by(email=user).first()
        if user and user.password == password:
            return user
        return None


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    urgent = db.Column(db.Boolean(), nullable=False)
    state = db.Column(db.String(5), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('todo', lazy=True))

    def __repr__(self):
        return f'Todo(name="{self.name}", description="{self.description}", urgent="{self.urgent}", state="{self.state}")'


def configure(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    app.db = db
