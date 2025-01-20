from flask import Flask,request
from urllib import request as request_api
from models import *
from flask_cors import CORS
import conexion
from hash import generarHash,validarPassword
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/login/usuarios',methods=["GET"])
def validarUsuario():
    usuario = request.args.get("username")
    contraseña = request.args.get("password")
    resultado = {"nombre":usuario,"valido":False}
    try:
        print(usuario+" ",contraseña)
        usuario = Usuarios.select().where(Usuarios.nombre==usuario).get()
        if(validarPassword(contraseña,usuario.sal,usuario.contraseña)):
            print("Sesion iniciada")
            resultado["valido"] = True
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
    for id_super in range(1,11):
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
        usuario = Usuarios.create(nombre=data["nombre"],contraseña=contraseña,sal=sal)
    except:
        print("Error") 
    return data


if __name__ == '__main__':

    db = conexion.conexion()

    db.connect()

    db.create_tables([Usuarios])

    app.run(host='0.0.0.0',port=5000)
