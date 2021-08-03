# ----- DATABASE MODELS ----------

from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

# --- Notes Schema *This schema can be changed to use in another app
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Colum(db.DateTime(timezone=True, default=func.now())
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))

    
# ---- User Schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    email =db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    notes = db.relationship('Note')
    
