from .db import db

class Camas(db.Model):
    habitacion_id = db.Column(db.Integer,db.ForeignKey("habitaciones.id"))
    nombre = db.Column(db.Enum("a","b"))
