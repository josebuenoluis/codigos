from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=45,primary_key=True)
    password = models.CharField(max_length=20)
    correo = models.CharField(max_length=80)

class Ciclos(models.Model):
    nombre = models.CharField(max_length=45,unique=True)

class Asignaturas(models.Model):
    nombre = models.CharField(max_length=60)
    id_ciclo_fk = models.ForeignKey(Ciclos,on_delete=models.PROTECT)

class Cuestionarios(models.Model):
    id_ciclo_fk = models.ForeignKey(Ciclos,on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now=True)

class Preguntas(models.Model):
    pregunta = models.TextField(null=False)
    id_cuestionario_fk = models.ForeignKey(Cuestionarios,on_delete=models.CASCADE)

class Respuestas(models.Model):
    respuesta = models.TextField(null=False)
    correcta = models.BooleanField(null=False)
    id_pregunta_fk = models.ForeignKey(Preguntas,on_delete=models.CASCADE)

class Estadisticas(models.Model):
    nombre_usuario_fk = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    id_ciclo_fk = models.ForeignKey(Ciclos,on_delete=models.CASCADE)
    acertadas = models.IntegerField(null=False)
    falladas = models.IntegerField(null=False)
    porcentaje_acierto = models.FloatField(null=False)

