from .db import db

class Habitaciones(db.Model):
    __tablename__ = "habitaciones"
    numero = db.Column(db.Integer)
    planta_fk = db.Column(db.Integer,db.ForeignKey("plantas.id"))

    def __init__(self,numero) -> None:
        self.numero = numero



