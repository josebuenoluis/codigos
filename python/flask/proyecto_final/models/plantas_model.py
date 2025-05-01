from .db import db

class Plantas(db.Model):
    numero = db.Column(db.Integer)