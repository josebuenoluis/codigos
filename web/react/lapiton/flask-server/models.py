from peewee import *
import conexion

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
    
