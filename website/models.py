from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# DB schema
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.string(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # referencing parent in one to many relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.string(150))
    first = db.Column(db.string(150))
    notes = db.relationship('Note')

