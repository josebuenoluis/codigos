from flask import render_template,Blueprint

asistencias = Blueprint("asistencias",__name__)

@asistencias.route("/asistencias/historico", methods=["GET"])
def historico_asistencias():
    return render_template("asistencias-historico.html")

@asistencias.route("/asistencias/consultas", methods=["GET"])
def consultas_asistencias():
    return render_template("asistencias-consultas.html")
