from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    urgent = db.Column(db.Boolean(), nullable=False)
    state = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f'Todo(name="{self.name}", description="{self.description}", urgent="{self.urgent}", state="{self.state}")'

def configure(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    app.db = db
