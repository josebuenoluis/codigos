from .db import db

class Camas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.Enum("a","b"))
    habitacion_fk = db.Column(db.Integer,db.ForeignKey("habitaciones.numero"))
