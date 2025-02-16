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