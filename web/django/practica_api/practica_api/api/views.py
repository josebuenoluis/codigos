from django.shortcuts import render
from .models import Proyectos,JefeProyecto
from rest_framework import viewsets
from .serializadores import ProyectosSerializer,JefeProyectoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.response import Response
# Create your views here.

class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer

    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)

class JefeProyectoViewSet(viewsets.ModelViewSet):
    queryset = JefeProyecto.objects.all()
    serializer_class = JefeProyectoSerializer

    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)
    def post(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)
    def put(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)
    def delete(self,request,format=None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)
    


