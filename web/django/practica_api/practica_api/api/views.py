from django.shortcuts import render
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