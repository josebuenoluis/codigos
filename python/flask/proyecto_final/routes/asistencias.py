from flask import render_template,Blueprint,request,send_file
from services import mariadb_service as db_service
from utils.utilidades_csv import exportarCSV
from os import path
asistencias = Blueprint("asistencias",__name__)

@asistencias.route("/asistencias/historico", methods=["GET"])
def historico_asistencias():
    return render_template("asistencias-historico.html")

@asistencias.route("/asistencias/consultas", methods=["GET"])
def consultas_asistencias():
    return render_template("asistencias-consultas.html")

@asistencias.route("/asistencias/exportar", methods=["GET","POST"])
def exportar_asistencias():
    if request.method == "GET":
        asistencias = db_service.obtener_asistencias()
        return render_template("exportar-datos.html",asistencias=asistencias)
    else:
        print("Dentro de post")
        data = request.get_json()
        # print(data)
        success = False
        if data:
            basepath = path.dirname(__file__)
            url_file = path.join(basepath,"static/archivos","prueba.csv")
            url_file = "C:/Users/Usuario/Documents/codigos/python/flask/proyecto_final/static/archivos/prueba.csv"
            success = True
            exportarCSV(data)
            return send_file(
                url_file,
                as_attachment=True,
                download_name="prueba.csv"
            )

        return {"success":success}

