from flask_login import UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def login(self, email, password):
        user = self.query.filter_by(email=email).first()
        if user and user.password == password:
            return user
        return None

    def register(self, name, email, password):
        try:
            user = User(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            return False


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    urgent = db.Column(db.Boolean(), nullable=False)
    state = db.Column(db.String(15), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('todo', lazy=True, cascade="all,delete")
    )

    def __repr__(self):
        return f'Todo(name="{self.name}", description="{self.description}", urgent="{self.urgent}", state="{self.state}")'  # NOQA


def configure(app):
    db.init_app(app)
    Migrate(app, db)
    app.db = db
