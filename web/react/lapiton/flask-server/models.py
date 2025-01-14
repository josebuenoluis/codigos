from peewee import *
import conexion

class BaseModel(Model):
    class Meta:
        database = conexion.conexion()
        force_insert = True

