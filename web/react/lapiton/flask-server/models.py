from peewee import *
import conexion
from datetime import datetime
db = conexion.conexion()

class BaseModel(Model):
    class Meta:
        database = db
        force_insert = True

class Usuarios(BaseModel):
    nombre = TextField()
    contraseña = TextField()
    sal = BlobField()
    avatar = TextField()
    
class Juegos(BaseModel):
    nombre = TextField()
    categoria = TextField()
    fondoIcono = TextField()
    fecha_lanzamiento = DateField(default=datetime.now())
    
