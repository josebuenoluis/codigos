<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class JefeProyecto(models.Model):
    dni_jefe_proyecto = models.CharField(max_length=9,primary_key=True)
    nombre_jefe = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre_jefe
#Modelo para proyectos
class Proyectos(models.Model):
    usuario = models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    nombre_proyecto = models.CharField(max_length=80)
    descripcion_proyecto = models.TextField()
    jefe_proyecto_fk = models.ForeignKey(JefeProyecto,on_delete=models.PROTECT)
    complete = models.BooleanField(default=False,verbose_name= "Completado")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_proyecto
=======
from django.db import models
from django.utils.timezone import now

class Usuarios(models.Model):
    dni_usuario = models.CharField(max_length=9,primary_key=True)
    nombre = models.CharField(max_length=200,verbose_name="nombre_usuario")

    def __str__(self):
        texto = f"""
        Nombre: {self.nombre}
        DNI: {self.dni_usuario}"""
        return texto

class Proyectos(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="titulo_proyecto")
    descripcion = models.TextField()
    presupuesto = models.FloatField()
    dni_usuario_fk = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    jefe_proyecto_fk = models.OneToOneField("Empleados",to_field="dni_empleado",on_delete=models.RESTRICT)
    created = models.DateTimeField(verbose_name="fecha_inicio",default=now)

    def __str__(self):
        texto = f"""
        Titulo: {self.titulo}
        Descripcion: {self.descripcion}
        DNI de usuario: {self.dni_usuario_fk}
        DNI de jefe de Proyecto: {self.jefe_proyecto_fk}
        Fecha de creacion: {self.created}"""
        return texto

class Empleados(models.Model):
    dni_empleado = models.CharField(max_length=9,primary_key=True,verbose_name="dni_empleado")
    nombre = models.CharField(max_length=80,verbose_name="nombre_empleado")
    id_proyecto_fk = models.ForeignKey(Proyectos,models.CASCADE)
    jefe_proyecto = models.BooleanField()

    def __str__(self):
        texto = f"""
        Nombre: {self.nombre}
        DNI: {self.dni_empleado}
        Id de proyecto: {self.id_proyecto_fk}"""
        return texto
    
    
>>>>>>> 1f322e2f831b8d0a1d643f6dc4d20b325f0186a3
