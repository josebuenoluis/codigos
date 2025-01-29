from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Task
# Create your views here.
class TaskView(View):
    def get(self,request):
        tasks = list(Task.objects.values())
        if tasks:
            datos = {'message':'Ok','tasks':tasks}
        else:
            datos = {'message':'No hay tareas que hacer'}
        return JsonResponse(datos)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass
    