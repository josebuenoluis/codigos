from peewee import *
from datetime import datetime
#Importamos fichero de conexion
import conexion

db = conexion.conexion()

#Creamos la tabla Base de la cual heredaran todas las tablas
class BaseModel(Model):
    class Meta:
        database = db
        force_insert = True

# Creamos tabla Empleados
class Empleados(BaseModel):
    dni_empleado = CharField(max_length=9,primary_key=True)
    nombre_empleado = CharField(max_length=20)
    puesto = BooleanField()
    email = CharField()

# Creamos la tabla Cliente
class Cliente(BaseModel):
    dni_cliente = CharField(max_length=9,primary_key=True)
    nombre_cliente = CharField(max_length=20)
    telefono = IntegerField()
    email = CharField()

#Creamos la tabla Proyectos
class Proyectos(BaseModel):
    id_proyecto = AutoField(primary_key=True)
    titulo_proyecto = CharField()
    descripcion = CharField()
    fecha_inicio = DateField(default=datetime.now())
    fecha_fin = DateField()
    presupuesto = FloatField()
    dni_cliente_fk = ForeignKeyField(Cliente,column_name = "dni_cliente_fk",on_update="CASCADE",on_delete="CASCADE")
    dni_jefe_proyecto_fk = ForeignKeyField(Empleados,column_name = "dni_jefe_proyecto_fk",on_update="CASCADE",on_delete="CASCADE")

#Creamos la tabla Empleados_Proyectos
class EmpleadosProyectos(BaseModel):
    id_proyecto_fk = ForeignKeyField(Proyectos,column_name="id_proyecto_fk",on_update="CASCADE",on_delete="CASCADE")
    dni_empleado_fk = ForeignKeyField(Empleados,column_name="dni_empleado_fk",on_update="CASCADE",on_delete="CASCADE")
    class Meta:
        table_name = "Empleados_Proyectos"
        primary_key = CompositeKey("id_proyecto_fk","dni_empleado_fk")
    
#Creamos la tabla Proyectos_Trabajados
class ProyectosTrabajados(BaseModel):
    old_id_proyecto = IntegerField()
    old_dni_empleado = CharField(max_length=9)
    class Meta:
        table_name = "Proyectos_Trabajados"

            