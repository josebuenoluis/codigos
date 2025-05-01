from .db import db

class Asistentes(db.Model):
    dni = db.Column(db.String(9),unique=True)
    nombre = db.Column(db.String(45))
    telefono = db.Column(db.Integer,unique=True)
    codigo = db.Column(db.String(6),unique=True)
    planta_fk = db.Column(db.Integer,unique=True)
    activo = db.Column(db.Boolean)
