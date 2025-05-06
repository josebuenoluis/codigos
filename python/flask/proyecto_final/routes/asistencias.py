from flask import render_template,Blueprint,request
from services import mariadb_service as db_service

asistencias = Blueprint("asistencias",__name__)

@asistencias.route("/asistencias/historico", methods=["GET"])
def historico_asistencias():
    return render_template("asistencias-historico.html")

@asistencias.route("/asistencias/consultas", methods=["GET"])
def consultas_asistencias():
    return render_template("asistencias-consultas.html")

@asistencias.route("/asistencias/exportar", methods=["GET"])
def exportar_asistencias():
    return render_template("exportar-datos.html")

