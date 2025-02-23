from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/inicio.html")

def galeria(request):
    return render(request,"core/galeria.html")