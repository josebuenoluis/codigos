from flask import Flask,request
from models import *
from flask_cors import CORS
import conexion

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
        usuario = {"nombre":usuario.nombre,"contraseña":usuario.contraseña}
    except:
        print("Error") 
        usuario = {}
    print(usuario)
    return usuario

if __name__ == '__main__':

    db = conexion.conexion()

    db.connect()

    app.run(host='0.0.0.0',port=5000)
