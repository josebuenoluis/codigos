from peewee import *

def conexion():
    db = MySQLDatabase("juego",host="localhost",port=3306,user="root",password="alumno")
    return db 