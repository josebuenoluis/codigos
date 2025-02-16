from rest_framework import serializers
from .models import JefeProyecto,Proyectos


class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = "__all__"

class JefeProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JefeProyecto
        fields = "__all__"