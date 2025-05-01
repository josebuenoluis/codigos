from .db import db
from datetime import datetime
import enum


class Asistencias(db.Model):
    habitacion_fk = db.Column(db.Integer,db.ForeignKey("habitaciones.id"))
    cama_fk = db.Column(db.Integer,db.ForeignKey("camas.id"))
    fecha_llamada = db.Column(db.DateTime,default=datetime.now())
    fecha_presencia = db.Column(db.DateTime,nullable=True)
    asistente_id = db.Column(db.Integer,nullable=True)
    estado = db.Column(db.Enum("pendiente","atendida","finalizada"))
