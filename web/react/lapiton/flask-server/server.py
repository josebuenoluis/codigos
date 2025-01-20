from flask import Flask,request
from models import *
from flask_cors import CORS
import conexion
from hash import generarHash,validarPassword

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/registrar/usuarios',methods=["GET"])
def consultaUsuario():
    data = request.args.get("username")
    print(data)
    try:
        usuario = Usuarios.select().where(Usuarios.nombre==data).get()
        usuario = {"nombre":usuario.nombre,"contraseña":usuario.contraseña,"sal":usuario.sal}
    except:
        print("Error") 
        usuario = {}
    print(usuario)
    return usuario

@app.route('/registrar/usuarios',methods=["POST"])
def crearUsuario():
    data = request.get_json()
    try:
        contraseña,sal = generarHash(data["contraseña"])
        usuario = Usuarios.create(nombre=data["nombre"],contraseña=contraseña,sal=str(sal))
    except:
        print("Error") 
    return data

if __name__ == '__main__':

    db = conexion.conexion()

    db.connect()

    db.create_tables([Usuarios])

    app.run(host='0.0.0.0',port=5000)
