from flask import Flask,request
from urllib import request as request_api
from models import *
from flask_cors import CORS
from datetime import timedelta
import conexion
from hash import generarHash,validarPassword
import json
from peewee import fn

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def index():    
    categoria = request.args.get("categoria")
    titulo = request.args.get("titulo")
    if categoria != None and categoria != "Categorias"\
        and titulo == None:
        juegos = Juegos.select().where(Juegos.categoria==categoria)
    elif categoria == None and titulo != None:
        juegos = Juegos.select().where(Juegos.nombre**f'%{titulo}%')
    elif categoria != None and categoria != "Categorias" and titulo != None:
        juegos = Juegos.select().where((Juegos.categoria==categoria)&(Juegos.nombre**f'%{titulo}%')) 
    else:
        juegos = Juegos.select()

    diccionario = {}
    for juego in juegos: 
        if juego.categoria not in diccionario:
            diccionario[juego.categoria] = []
        objeto_juego = {}
        objeto_juego["nombre"] = juego.nombre
        objeto_juego["fondoIcono"] = juego.fondoIcono
        diccionario[juego.categoria].append(objeto_juego)
    return diccionario

@app.route("/juego/relacionados")
def obtenerJuegosRelacionados():
    titulo = request.args.get("titulo")
    diccionario = {}
    if titulo != "" and titulo != None:
        try:
            categoria = Juegos.select(Juegos.categoria).distinct().where(Juegos.nombre==titulo).get().categoria
            juegos = Juegos.select().where(Juegos.categoria==categoria)
            diccionario = {}
            for juego in juegos: 
                if juego.categoria not in diccionario:
                    diccionario[juego.categoria] = []
                objeto_juego = {}
                objeto_juego["nombre"] = juego.nombre
                objeto_juego["fondoIcono"] = juego.fondoIcono
                diccionario[juego.categoria].append(objeto_juego)
        except:
            diccionario = {}
    return diccionario
@app.route("/ranking",methods=["GET"])
def ranking():
    #Ejecutamos una consulta para obtener a los 10 o tantos mejores jugadores,
    #segun los filtros aplicados, los filtros seran pasados
    # en los Headers de la peticion
    filtro_categoria = request.args.get("categoria")
    filtro_busqueda = request.args.get("busqueda")
    
    data = {}
    juegos = Juegos.select(Juegos.categoria).distinct()
    if filtro_categoria == None and filtro_busqueda == None:
        jugadores = Ranking.select(
            Ranking.usuario_fk,Ranking.juego,Ranking.categoria,fn.MAX(Ranking.dificultad),fn.MAX(Ranking.puntaje)
        ).group_by(Ranking.usuario_fk,Ranking.juego,Ranking.categoria).order_by(fn.MAX(Ranking.puntaje).desc()).limit(10)
    elif filtro_categoria != None and filtro_busqueda == None:
        jugadores = Ranking.select(
            Ranking.usuario_fk,Ranking.juego,Ranking.categoria,fn.MAX(Ranking.dificultad),fn.MAX(Ranking.puntaje)
        ).where(Ranking.categoria==filtro_categoria).group_by(Ranking.usuario_fk,Ranking.juego,Ranking.categoria).order_by(fn.MAX(Ranking.puntaje).desc()).limit(10)
    elif filtro_categoria == None and filtro_busqueda != None:
        jugadores = Ranking.select(
            Ranking.usuario_fk,Ranking.juego,Ranking.categoria,fn.MAX(Ranking.dificultad),fn.MAX(Ranking.puntaje)
        ).where(
            Ranking.juego**f'%{filtro_busqueda}%'
        ).group_by(Ranking.usuario_fk,Ranking.juego,Ranking.categoria).order_by(fn.MAX(Ranking.puntaje).desc()).limit(10)
    elif filtro_categoria != None and filtro_busqueda != None:
        jugadores = Ranking.select(
            Ranking.usuario_fk,Ranking.juego,Ranking.categoria,fn.MAX(Ranking.dificultad),fn.MAX(Ranking.puntaje)
        ).where(
            (Ranking.categoria==filtro_categoria) &
            (Ranking.juego**f'%{filtro_busqueda}%')
        ).group_by(Ranking.usuario_fk,Ranking.juego,Ranking.categoria).order_by(fn.MAX(Ranking.puntaje).desc()).limit(10)
    listaCategorias = []
    listaJugadores = []
    #Para obtener la lista de categorias
    for juego in juegos:
        listaCategorias.append(juego.categoria)
    # #Para obtener el top de los jugadores
    for jugador in jugadores:
        listaJugadores.append({"puntaje":jugador.puntaje,"dificultad":jugador.dificultad,"nombre":jugador.usuario_fk.nombre,"juego":jugador.juego,"categoria":jugador.categoria})

    data["categorias"] = listaCategorias
    data["jugadores"] = listaJugadores
    return data

@app.route("/ranking/puntos",methods=["POST"])
def rankingPuntos():
    data = request.get_json()
    try:
        # Guardamos los puntos del usuario en la tabla ranking con el 
        #nombre del juego y la categoria del juego, hay que consultar
        # el puntaje mas alto de ese usuario y si es mas alto lo guardamos
        # y si no, no lo guardaremos en la tabla ranking, sera otra tabla a futuro.
        # 
        Ranking.create(puntaje=data["puntaje"],dificultad=data["dificultad"],juego=data["juego"],categoria=data["categoria"],usuario_fk=data["nombre"])
        print("Puntos guardados correctamente.")
    except Exception as error:
        print(f"Error: {error}")
    return data

@app.route('/login/usuarios',methods=["GET"])
def validarUsuario():
    usuario = request.args.get("username")
    contraseña = request.args.get("password")
    resultado = {"nombre":usuario,"valido":False}
    try:
        usuario = Usuarios.select().where(Usuarios.nombre==usuario).get()
        if(validarPassword(contraseña,usuario.sal,usuario.contraseña)):
            resultado["valido"] = True
            resultado["avatar"] = usuario.avatar
        else:
            print("Contraseña incorrecta")
            resultado["valido"] = False
    except Exception as error:
        print(f"Error: {error}")
        resultado["valido"] = False
    return resultado

@app.route('/registrar/usuarios',methods=["GET"])
def consultaUsuario():
    data = request.args.get("username")
    try:
        usuario = Usuarios.select().where(Usuarios.nombre==data).get()
        usuario = {"nombre":usuario.nombre,"contraseña":usuario.contraseña}
    except:
        print("Error") 
        usuario = {}
    print(usuario)
    return usuario

@app.route('/registrar/avatars',methods=["GET"])
def listarAvatars():
    resultado = []
    for id_super in range(1,13):
        response = request_api.urlopen(f"https://superheroapi.com/api/7693742abd0d2968a66bc4d38f33db24/{id_super}")
        data = response.read()
        data = data.decode("utf-8")
        avatar = json.loads(data.split("\n")[-1])
        imagen = avatar["image"]["url"]
        resultado.append({"id_avatar":id_super,"imagen":imagen})
    return resultado

@app.route('/registrar/usuarios',methods=["POST"])
def crearUsuario():
    data = request.get_json()
    try:
        contraseña,sal = generarHash(data["contraseña"])
        usuario = Usuarios.create(nombre=data["nombre"],contraseña=contraseña,sal=sal,avatar=data["avatar"])
    except Exception as error:
        print("Error: ",error) 
    return data


@app.route("/novedades/agregar",methods=["POST"])
def subirNovedad():
    data = request.get_json()
    try:
        novedad = Novedades.create(titulo=data["titulo"],descripcion=data["descripcion"]
                                   ,imagen=data["imagen"])
        print(f"Novedad subida con exito.")
        data["subida"] = True
    except Exception as error:
        print("Error: ",error) 
        data["subida"] = False
    return data

@app.route("/novedades",methods=["GET"])
def obtenerNovedades():
    novedades = Novedades.select()
    listaNovedades = []
    for novedad in novedades:
        diccionario = {}
        diccionario["titulo"] = novedad.titulo
        diccionario["imagen"] = novedad.imagen
        diccionario["descripcion"] = novedad.descripcion
        listaNovedades.append(diccionario)
    return listaNovedades

@app.route("/novedades/novedad")
def obtenerNovedad():
    titulo = request.args.get("titulo")
    data = {}
    try:
        novedad = Novedades.select().where(Novedades.titulo==titulo).get()
        data["titulo"] = novedad.titulo
        data["imagen"] = novedad.imagen
        data["descripcion"] = novedad.descripcion
        print(f"Novedad obtenida con exito.")
    except Exception as error:
        print("Error: ",error) 
    return data

@app.route("/novedades/eliminar",methods=["DELETE"])
def eliminarNovedad():
    titulo = request.args.get("titulo")
    clave = request.args.get("clave")
    user_admin = Usuarios.select().where(Usuarios.nombre=="admin").get()
    data = {}
    if(validarPassword(clave,user_admin.sal,user_admin.contraseña)):            
        try:
            novedad = Novedades.delete().where(Novedades.titulo==titulo).execute()
            data["realizada"] = True
            print(f"Novedad eliminada con exito.")
        except Exception as error:
            print("Error: ",error) 
            data["realizada"] = False
    return data

@app.route("/preguntas")
def obtenerPreguntas():
    preguntas = Preguntas.select()
    data = []
    for pregunta in preguntas:
        diccionario = {}
        diccionario["pregunta"] = pregunta.pregunta
        diccionario["respuesta"] = pregunta.respuesta
        diccionario["fecha_pregunta"] = pregunta.fecha_pregunta
        data.append(diccionario)
    return data

if __name__ == '__main__':

    db = conexion.conexion()

    db.connect()

    db.create_tables([Usuarios,Juegos,Ranking,Novedades,Preguntas])

    app.run(host='0.0.0.0',port=5000)
