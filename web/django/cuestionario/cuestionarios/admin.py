from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Usuarios,Ciclos,Asignaturas,Preguntas,
                     Respuestas,Estadisticas,Cuestionarios])