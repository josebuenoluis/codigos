from django.shortcuts import render
from django.core import serializers
from django.views import View
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Task
from .serializador import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.response import Response 
import json
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format = None):
        content = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        return Response(content)

class TaskView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        tasks = list(Task.objects.values())
        if tasks:
            datos = {'message':'Ok','tasks':tasks}
        else:
            datos = {'message':'No hay tareas que hacer'}
        return JsonResponse(datos)
    
    def get(self,request,pk=0):
        if pk > 0:
            tasks = list(Task.objects.filter(id=pk).values())
            if tasks:
                task = tasks[0]
                datos = {"message":"OK","tareas":task}
            else:
                datos = {"message":"No hay tareas con ese ID"}

        else:
            tasks = list(Task.objects.values())
            if tasks:
                datos = {'message':'Ok','tasks':tasks}
            else:
                datos = {'message':'No hay tareas que hacer'}
        return JsonResponse(datos)
    

    def post(self,request):
        jd = json.loads(request.body)
        Task.objects.create(
            title = jd["title"],
            description = jd["description"],
            complete = jd["complete"]
        )
        datos = {"message":"Datos insertados correctamente"}
        return JsonResponse(datos)
    
    def put(self,request,pk=0):
        jd = json.loads(request.body)
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            task = Task.objects.get(id=pk)
            task.title = jd["title"]
            task.description = jd["description"]
            task.complete = jd["complete"]
            task.save()
            datos = {"message":"Datos modificados."}
        else:
            datos = {"message":"Tarea no encontrada."}
        return JsonResponse(datos)

    def delete(self,request,pk=0):
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            task = Task.objects.get(id=pk)
            datos = {"message":"Datos borrados."}
        else:
            datos = {"message":"Tarea no encontrada."}
        return JsonResponse(datos)

class TaskViewXML(View):
    def get(self,request):
        data = serializers.serialize('xml',Task.objects.all())
        return HttpResponse(data)
    