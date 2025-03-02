from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
from .models import *
from .utils import *
import json
# Create your views here.

class CuestionariosView(View):
    def get(self,request):
        return render(request,"cuestionarios/cuestionarios.html")


class CrearCuestionarioView(View):
    def get(self,request):
        return render(request,"cuestionarios/cuestionario.html")
    
    def post(self,request):
        # print(request)
        # print(request.POST["archivo"])
        print(request.FILES["archivo"])
        archivo = request.FILES["archivo"]
        print(request.POST)
        print(request.POST.get('ciclo'))
        nombre_cuestionario = request.POST["nombre"]
        tema_asignatura = request.POST["tema"]
        # ciclo = request.POST["ciclo"]
        # asignatura = request.POST["asignatura"]
        # preguntas = request.POST[""]
        # print(extraer_texto_pdf_directo(archivo))
        texto_pdf = extraer_texto_pdf_directo(archivo)
        cuestionario = procesar_pdf_y_generar_cuestionario_json(texto_pdf,total_preguntas=10)
        # print(cuestionario)

        return JsonResponse({"cuestionario":cuestionario})
    
