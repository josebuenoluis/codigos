from flask import Flask
from peewee import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/subir")
def subir():
    pass


def conexion():
    return MySQLDatabase("prueba",host="localhost",port=3306,user="root",password="alumno")

class User(Model):
    nombre = CharField(max_length=80)

if __name__ == '__main__':

    db = conexion()

    db.connect()

    db.create_tables([User])

    app.run(host="0.0.0.0",port=5000)
