from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import *
from .utils import *
import math
import json
# Create your views here.

class CuestionariosView(View):


    def get(self,request,n_pagina=1):
        busqueda = request.GET.get('busqueda', '')
        ciclo = request.GET.get('ciclo','')
        asignatura = request.GET.get('asignatura','')
        filtros = request.GET.get('filtros','')
        if busqueda != "":
            n_pagina = 1
        #El numero de pagina se utilizara para seleccionar los cuestionario atraves de 
        #una especie de indicie, una pagina tiene 8 cuestionarios y si es la pagina 1
        #se mostraran los primero 8 cuestionario y asi sucesivamente
        indice = n_pagina * 8
        desde = indice - 8
        cuestionarios_mostrar = []
        if filtros:
            if ciclo != "" and asignatura == "" and busqueda == "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(id_ciclo_fk=ciclo)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo == "" and asignatura != "" and busqueda == "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(id_asignatura_fk=asignatura)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo != "" and asignatura != "" and busqueda == "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(id_ciclo_fk=ciclo,id_asignatura_fk=asignatura)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo != "" and asignatura != "" and busqueda != "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(id_ciclo_fk=ciclo,id_asignatura_fk=asignatura,nombre_cuestionario__icontains=busqueda)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo != "" and asignatura == "" and busqueda != "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(id_ciclo_fk=ciclo,nombre_cuestionario__icontains=busqueda)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo == "" and asignatura != "" and busqueda != "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(nombre_cuestionario__icontains=busqueda,id_asignatura_fk=asignatura)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo == "" and asignatura == "" and busqueda != "":
                cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(nombre_cuestionario__icontains=busqueda)
                cuestionarios_mostrar = cuestionarios[desde:indice]
            elif ciclo == "" and asignatura == "" and busqueda == "":
                cuestionarios_mostrar = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').all()[desde:indice]
            return render(request,"cuestionarios/cuestionarios-filtros.html",{"cuestionarios":cuestionarios_mostrar})
        elif busqueda:
            cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').filter(nombre_cuestionario__icontains=busqueda)
        else:
            cuestionarios = Cuestionarios.objects.select_related('id_ciclo_fk').select_related('id_asignatura_fk').all()
        cuestionarios_mostrar = cuestionarios[desde:indice]
        n_cuestionarios = len(cuestionarios)
        n_paginas = n_cuestionarios / 8
        n_paginas = math.ceil(n_paginas)
        numeracion = [{"indice":n,"ruta":f"/cuestionarios/{n}"} for n in range(1,n_paginas+1)]
        #Si la pagina es divisible entre 5 es que hay que mostrar los siguientes numeros porque
        # este en el inicio o final de los 5 indices
        if n_pagina % 5 == 0 or n_pagina == 1:
            inicio = (n_pagina - 1) // 5 * 5
            fin = inicio + 5
            numeracion = numeracion[inicio:fin]
            siguiente = n_pagina + 1 if n_pagina < n_paginas else n_pagina
            anterior = n_pagina - 1 if n_pagina > 1 else 1
        else:
            inicio = (n_pagina - 1) // 5 * 5
            fin = inicio + 5
            numeracion = numeracion[inicio:fin]
            siguiente = n_pagina + 1 if n_pagina < n_paginas else n_pagina
            anterior = n_pagina - 1 if n_pagina > 1 else 1
        return render(request,"cuestionarios/cuestionarios.html",{"cuestionarios":cuestionarios_mostrar,"indices":numeracion,
                    "siguiente":siguiente,"anterior":anterior})

class CrearCuestionarioView(View):

    def get(self,request):

        ciclos = Ciclos.objects.all()
        asignaturas = Asignaturas.objects.all()

        return render(request,"cuestionarios/cuestionario.html",{"ciclos":ciclos,"asignaturas":asignaturas})
    
    def post(self,request):
        try:
            #Obtenemos el archivo PDF enviado por el formulario
            archivo = request.FILES["archivo"]
            # Obtenemos los datos enviados por el formulario
            nombre_cuestionario = request.POST["nombre"]
            tema_asignatura = request.POST["tema"]
            ciclo = request.POST["ciclo"]
            asginatura = request.POST["asignatura"]
            preguntas = request.POST["preguntas"]
            respuestas = request.POST["respuestas"]
            # correctas = request.POST["correctas"] if request.POST["correctas"] != "" else "1"
            descripcion = request.POST["descripcion"]
            enlace = request.POST["enlace"]
            #Obtenemos el texto del PDF y generamos el cuestionario
            texto_pdf = extraer_texto_pdf_directo(archivo)
            cuestionario_generado = procesar_pdf_y_generar_cuestionario_json(texto_pdf,total_preguntas=int(preguntas),
                                    n_respuestas=int(respuestas))
            if enlace == "guardar_contestar":
                #Guardamo el cuestionario en y mandamos al usuario a contestarlo
                cuestionario = Cuestionarios(
                    nombre_cuestionario=nombre_cuestionario,
                    tema_asignatura_cuestionario=tema_asignatura,
                    id_ciclo_fk=Ciclos.objects.get(nombre=ciclo),
                    id_asignatura_fk=Asignaturas.objects.get(nombre=asginatura),
                    nombre_usuario_fk=Usuarios.objects.get(nombre="jose"),
                    descripcion_cuestionario=descripcion
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
            elif enlace == "generar":
                
                return HttpResponse(cuestionario_generado)

        except Exception as error:
            print("Error: ",error)
    

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
        respuestas = Respuestas.objects.filter(id_pregunta_fk__in=preguntas)
        preguntas_respuestas = [
            {
                "pregunta": pregunta,
                "respuestas": [respuesta for respuesta in respuestas if respuesta.id_pregunta_fk == pregunta]
            }
            for pregunta in preguntas
        ]
        for id_pregunta in request.POST:
            if id_pregunta.isdigit():
                respuesta_correcta = Respuestas.objects.get(id_pregunta_fk=id_pregunta,correcta=True)
                respuesta_usuario = request.POST[id_pregunta]
                respuesta_usuario_objeto = Respuestas.objects.get(id=respuesta_usuario,id_pregunta_fk=id_pregunta)
                cuestionario = Cuestionarios.objects.get(id=cuestionario_id)
                acierto = False
                if int(respuesta_usuario) == respuesta_correcta.id:
                    print(f"Usuario acerto en la pregunta {id_pregunta} y en la respuesta {respuesta_correcta.respuesta}")
                    acierto = True
                else:
                    print(f"Usuario fallo en la pregunta {id_pregunta} y en la respuesta {respuesta_usuario}")
                    acierto = False
                
                for pregunta in preguntas_respuestas:
                    if int(id_pregunta) == pregunta["pregunta"].id:
                        pregunta["acierto"] = acierto
                        pregunta["respuesta_correcta"] = respuesta_correcta
                        pregunta["respuesta_usuario"] = respuesta_usuario_objeto
                        print("respuesta usuario: ",respuesta_usuario_objeto.id)
                        
                print(f"Respuesta correcta es: {respuesta_correcta.respuesta} y el usuario respondio {respuesta_usuario}")
                
                respuestas_usuario_correctas_falladas.append({id_pregunta:{"correcta":respuesta_correcta.id,"usuario":respuesta_usuario}})
        
        print(preguntas_respuestas)
        return render(request,"cuestionarios/contestado.html",{"respuesta_usuario":respuestas_usuario_correctas_falladas,
                                                             "preguntas":preguntas_respuestas,"cuestionario":cuestionario})