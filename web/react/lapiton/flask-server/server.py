from flask import Flask,request,session
from urllib import request as request_api
from models import *
from flask_cors import CORS
from datetime import timedelta
import conexion
from hash import generarHash,validarPassword
import json

app = Flask(__name__)
CORS(app)
app.secret_key = "prueba1234"

@app.route("/",methods=["GET"])
def index():    
    juegos = Juegos.select()
    listaJuegos = []
    for juego in juegos:
        diccionario = {}
        diccionario["nombre"] = juego.nombre
        diccionario["fondoIcono"] = juego.fondoIcono
        listaJuegos.append(diccionario)
    return listaJuegos

@app.route("/ranking",methods=["GET"])
def ranking():
    juegos = Juegos.select(Juegos.categoria).distinct()
    listaCategorias = []
    for juego in juegos:
        listaCategorias.append(juego.categoria)
    print(listaCategorias)
    return listaCategorias

@app.route("/ranking/puntos",methods=["POST"])
def rankingPuntos():
    darta = request.get_json()

@app.route('/login/usuarios',methods=["GET"])
def validarUsuario():
    usuario = request.args.get("username")
    contraseña = request.args.get("password")
    resultado = {"nombre":usuario,"valido":False}
    try:
        usuario = Usuarios.select().where(Usuarios.nombre==usuario).get()
        if(validarPassword(contraseña,usuario.sal,usuario.contraseña)):
            print(f"NOmbre prueba sesion: {session}")
            session["nombre"] = usuario.nombre
            session["avatar"] = usuario.avatar
            resultado["valido"] = True
            resultado["avatar"] = usuario.avatar
            print(f"Sesion en Inicio de sesion: {session}")
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
    print(data)
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
        avatar = json.loads(response.read().decode("utf-8"))
        imagen = avatar["image"]["url"]
        resultado.append({"id_avatar":id_super,"imagen":imagen})
    print(resultado)
    return resultado

@app.route('/registrar/usuarios',methods=["POST"])
def crearUsuario():
    data = request.get_json()
    try:
        contraseña,sal = generarHash(data["contraseña"])
        usuario = Usuarios.create(nombre=data["nombre"],contraseña=contraseña,sal=sal,avatar=data["avatar"])
        session.permanent = True
        session["nombre"] = usuario.nombre
        session["avatar"] = usuario.avatar
        print(f"Sesion iniciada en crear usuario: {session}")
    except Exception as error:
        print("Error: ",error) 
    return data


if __name__ == '__main__':

    login = ""

    db = conexion.conexion()

    db.connect()

    db.create_tables([Usuarios,Juegos])

    app.run(host='0.0.0.0',port=5000)
