from django.shortcuts import render
<<<<<<< HEAD
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
    


=======
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Usuarios,Proyectos,Empleados
import json
# Create your views here.
class UsuariosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        usuarios = list(Usuarios.objects.values())
        if usuarios:
            datos = {"message":"ok","Usuarios":usuarios}
        else:
            datos = {"message":"No hay usuarios registrados."}
        return JsonResponse(datos)
    
    def post(self,request):
        usuario = json.loads(request.body)
        print(usuario)
        Usuarios.objects.create(
            dni_usuario = usuario["dni_usuario"],
            nombre = usuario["nombre"]
        )
        datos = {"message":"Usuario registrado correctamente!"}
        return JsonResponse(datos)
>>>>>>> 1f322e2f831b8d0a1d643f6dc4d20b325f0186a3
