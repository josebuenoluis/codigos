from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def cuestionarios(request):
    return render(request,"cuestionarios/cuestionarios.html")




def crear_cuestionario(request):
    print(request.POST)
    # print(request.POST["archivo"])
    # print(request.POST["nombre"])
    # print(request.POST["preguntas"])
    # print(request.POST["respuestas"])
    # print(request.POST["correctas"])
    return render(request,"cuestionarios/cuestionario.html")