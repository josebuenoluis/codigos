from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
from .models import *
from .utils import *
import json
# Create your views here.

class CuestionariosView(View):


    def get(self,request):
        cuestionarios = Cuestionarios.objects.all()
        return render(request,"cuestionarios/cuestionarios.html",{"cuestionarios":cuestionarios})


class CrearCuestionarioView(View):

    def get(self,request):

        ciclos = Ciclos.objects.all()
        asignaturas = Asignaturas.objects.all()

        return render(request,"cuestionarios/cuestionario.html",{"ciclos":ciclos,"asignaturas":asignaturas})
    
    def post(self,request):
        #Obtenemos el archivo PDF enviado por el formulario
        archivo = request.FILES["archivo"]
        print(request.POST)
        # Obtenemos los datos enviados por el formulario
        nombre_cuestionario = request.POST["nombre"]
        tema_asignatura = request.POST["tema"]
        ciclo = request.POST["ciclo"]
        asginatura = request.POST["asignatura"]
        preguntas = request.POST["preguntas"]
        respuestas = request.POST["respuestas"]
        correctas = request.POST["correctas"]
        descripcion = request.POST["descripcion"]
        enlace = request.POST["enlace"]
        #Obtenemos el texto del PDF y generamos el cuestionario
        texto_pdf = extraer_texto_pdf_directo(archivo)
        cuestionario_generado = procesar_pdf_y_generar_cuestionario_json(texto_pdf,total_preguntas=int(preguntas),
                                n_respuestas=int(respuestas),n_correctas=int(correctas))
        if enlace == "guardar_contestar":
            #Guardamo el cuestionario en y mandamos al usuario a contestarlo
            cuestionario = Cuestionarios(
                nombre_cuestionario=nombre_cuestionario,
                tema_asignatura_cuestionario=tema_asignatura,
                id_ciclo_fk=Ciclos.objects.get(nombre=ciclo),
                nombre_usuario_fk=Usuarios.objects.get(nombre="jose"),
                descripcion_cuestionario=descripcion,
            )
            
            cuestionario.save()
            
            preguntas = [Preguntas(pregunta=pregunta["pregunta"],id_cuestionario_fk=cuestionario) for pregunta in cuestionario_generado]
            
            for pregunta in preguntas:
                pregunta.save()

            respuestas = []
            for posicion_pregunta in range(len(cuestionario_generado)):
                for respuesta in cuestionario_generado[posicion_pregunta]["opciones"]:
                    respuestas.append(Respuestas(respuesta=respuesta,
                    correcta=True if cuestionario_generado[posicion_pregunta]["opciones"][cuestionario_generado[posicion_pregunta]["respuesta_correcta"]] == respuesta else False,
                    id_pregunta_fk=preguntas[posicion_pregunta]))
            
            for respuesta in respuestas:
                respuesta.save()

            return redirect("contestar_cuestionario",cuestionario_id=cuestionario.id)


        # return JsonResponse({"cuestionario":cuestionario_generado})
    

class ContestarCuestionarioView(View):


    def get(self,request,cuestionario_id):
        cuestionario = Cuestionarios.objects.get(id=cuestionario_id)
        preguntas = Preguntas.objects.filter(id_cuestionario_fk=cuestionario)
        respuestas = Respuestas.objects.filter(id_pregunta_fk__in=preguntas)
        preguntas_respuestas = [
            {
                "pregunta": pregunta,
                "respuestas": [respuesta for respuesta in respuestas if respuesta.id_pregunta_fk == pregunta]
            }
            for pregunta in preguntas
        ]
        return render(request, "cuestionarios/contestar.html", {"cuestionario": cuestionario, "preguntas": preguntas_respuestas,})

    def post(self,request,cuestionario_id):

        preguntas = Preguntas.objects.filter(id_cuestionario_fk=cuestionario_id)
        respuestas_usuario_correctas_falladas = []
        for id_pregunta in request.POST:
            if id_pregunta.isdigit():
                respuesta_correcta = Respuestas.objects.get(id_pregunta_fk=id_pregunta,correcta=True)
                respuesta_usuario = request.POST[id_pregunta]
                if int(respuesta_usuario) == respuesta_correcta.id:
                    print(f"Usuario acerto en la pregunta {id_pregunta} y en la respuesta {respuesta_correcta}")
                else:
                    print(f"Usuario fallo en la pregunta {id_pregunta} y en la respuesta {respuesta_usuario}")
                print(f"Respuesta correcta es: {respuesta_correcta.respuesta} y el usuario respondio {respuesta_usuario}")
                respuestas_usuario_correctas_falladas.append({id_pregunta:{"correcta":respuesta_correcta.id,"usuario":respuesta_usuario}})
        
        
        return redirect("cuestionarios")