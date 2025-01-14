from peewee import *

def conexion():
    db = MySQLDatabase("empresa",host="localhost",port=3306,user="root",password="alumno")
    return db