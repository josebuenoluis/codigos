from django.shortcuts import render
from django.views import View
from .models import Proyectos,JefeProyecto
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json
from django.db.models import ProtectedError
from rest_framework import viewsets
from .serializadores import ProyectosSerializer,JefeProyectoSerializer
from django.core import serializers
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
    


class ProyectosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,pk=0):
        
        if pk > 0:
            proyectos = list(Proyectos.objects.filter(id=pk).values())
            if proyectos:
                proyecto = proyectos[0]
                datos = {"message":"OK","Proyectos":proyecto}
            else:
                datos = {"message":"No hay proyectos con el ID ingresado."}
        else:
        
            proyectos = list(Proyectos.objects.values())
            if proyectos:
                datos = {"message":"Ok","Proyectos":proyectos}
            else:
                datos = {"message":"No hay proyectos"}
        return JsonResponse(datos)
    
    def post(self,request):
        print(request.body)
        jd = json.loads(request.body)
        print(jd)
        try:
            usuario = User.objects.get(username=jd["usuario"])
            jefe_proyecto = JefeProyecto.objects.get(dni_jefe_proyecto=jd["jefe_proyecto_fk"])
            Proyectos.objects.create(
                usuario = usuario,
                nombre_proyecto = jd["nombre_proyecto"],
                descripcion_proyecto = jd["descripcion_proyecto"],
                jefe_proyecto_fk = jefe_proyecto
            )
            datos = {"message":"Datos insertados correctamente."}
        except User.DoesNotExist:
            datos = {"message":"El usuario ingresado no existe."}
        except JefeProyecto.DoesNotExist:
            datos = {"message":"El Jefe de proyecto ingresado no existe."}
        except:
            datos = {"message":"Error al crear proyecto."}
        return JsonResponse(datos)
    
    def put(self,request,pk=0):
        jd = json.loads(request.body)
        proyectos = list(Proyectos.objects.filter(id=pk).values())
        if proyectos:
            try:
                proyecto = Proyectos.objects.get(id=pk)
                proyecto.nombre_proyecto = jd["nombre_proyecto"]
                usuario = User.objects.get(username=jd["usuario"])
                proyecto.usuario = usuario if usuario else proyecto.usuario
                proyecto.descripcion_proyecto = jd["descripcion_proyecto"]
                jefe_proyecto_fk = JefeProyecto.objects.get(dni_jefe_proyecto=jd["jefe_proyecto"])
                proyecto.jefe_proyecto_fk = jefe_proyecto_fk if jefe_proyecto_fk else proyecto.jefe_proyecto_fk
                proyecto.save()
                datos = {"message":"Proyecto actualizado correctamente."}
            except User.DoesNotExist:
                datos = {"message":"Usuario no encontrado."}
            except JefeProyecto.DoesNotExist:
                datos = {"message":"Jefe de proyecto no encontrado."}
            except:
                datos = {"message":"Error al actualizar proyecto."}
        else:
            datos = {"message":"Proyecto no encontrado."}
        return JsonResponse(datos)
            

    def delete(self,request,pk=0):
        proyectos = list(Proyectos.objects.filter(id=pk).values())
        if proyectos:
            Proyectos.objects.filter(id=pk).delete()
            datos = {"message":"Proyecto eliminado correctamente."}
        else:
            datos = {"message":"Proyecto no encontrado."}
        return JsonResponse(datos)
    
class JefeProyectoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,dni=""):
        
        if dni != "":
            jefes_proyectos = list(JefeProyecto.objects.filter(dni_jefe_proyecto=dni).values())
            if jefes_proyectos:
                jefe_proyecto = jefes_proyectos[0]
                datos = {"message":"OK","Proyectos":jefe_proyecto}
            else:
                datos = {"message":"No hay jefes de proyectos con el ID ingresado."}
        else:
            jefes_proyectos = list(JefeProyecto.objects.values())
            if jefes_proyectos:
                datos = {"message":"Ok","Jefes de proyecto":jefes_proyectos}
            else:
                datos = {"message":"No hay Jefes de proyecto"}
        return JsonResponse(datos)
    def post(self,request):
        print(request.body)
        jd = json.loads(request.body)
        print(jd)
        JefeProyecto.objects.create(
            dni_jefe_proyecto = jd["dni_jefe_proyecto"],
            nombre_jefe = jd["nombre_jefe"]
        )
        datos = {"message":"Datos insertados correctamente."}
        return JsonResponse(datos)
    
    def put(self,request,dni=""):
        jd = json.loads(request.body)
        jefes_proyectos = list(JefeProyecto.objects.filter(dni_jefe_proyecto=dni).values())
        if jefes_proyectos:
            jefe = JefeProyecto.objects.get(dni_jefe_proyecto=dni)
            jefe.nombre_jefe = jd["nombre_jefe"]
            jefe.save()
            datos = {"message":"Jefe actualizado correctamente."}
        else:
            datos = {"message":"Jefe de proyecto no encontrado."}
        return JsonResponse(datos)
    
    def delete(self,request,dni=""):
        jefes_proyectos = list(JefeProyecto.objects.filter(dni_jefe_proyecto=dni).values())
        if jefes_proyectos:
            try:
                JefeProyecto.objects.filter(dni_jefe_proyecto=dni).delete()
                datos = {"message":"Jefe de proyecto eliminado correctamente."}
            except ProtectedError:
                datos = {"message":"Este jefe de proyecto se encuentra en un proyecto."}
        else:
            datos = {"message":"Jefe de proyecto no encontrado."}
        return JsonResponse(datos)
    
class JefeProyectosViewXML(View):
    def get(self,request):
        data = serializers.serialize("xml",JefeProyecto.objects.all())
        return HttpResponse(data)

class ProyectosViewXML(View):
    def get(self,request):
        data = serializers.serialize("xml",Proyectos.objects.all())
        return HttpResponse(data)
