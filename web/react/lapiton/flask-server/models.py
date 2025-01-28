from peewee import *
import conexion
from datetime import datetime
db = conexion.conexion()

class BaseModel(Model):
    class Meta:
        database = db
        force_insert = True

class Usuarios(BaseModel):
    nombre = CharField(primary_key=True,max_length=20)
    contraseña = TextField()
    sal = BlobField()
    avatar = TextField()
    
class Juegos(BaseModel):
    nombre = TextField()
    categoria = TextField()
    fondoIcono = TextField()
    fecha_lanzamiento = DateField(default=datetime.now())

class Ranking(BaseModel):
    puntaje = IntegerField()
    juego = TextField()
    categoria = TextField()
    dificultad = IntegerField()
    usuario_fk = ForeignKeyField(Usuarios,column_name = "usuario_fk",on_update="CASCADE",on_delete="CASCADE")


