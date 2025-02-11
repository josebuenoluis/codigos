from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Usuarios,Proyectos,Empleados
import json
# Create your views here.
class UsuariosView(View):

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