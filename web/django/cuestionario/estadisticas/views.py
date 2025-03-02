from django.shortcuts import render

# Create your views here.
def estadisticas(request):
    return render(request,'estadisticas/estadisticas.html')