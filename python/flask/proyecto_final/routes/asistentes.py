from flask import render_template,Blueprint

asistentes = Blueprint("asistentes",__name__)

@asistentes.route("/asistentes/crear", methods=["GET"])
def crear_asistente():
    return render_template("crear-asistente.html")

@asistentes.route("/asistentes/modificar", methods=["GET"])
def modificar_asistente():
    return render_template("asistentes-modificar.html")

@asistentes.route("/asistentes/estadisticas", methods=["GET"])
def estadisticas_asistente():
    return render_template("asistentes-estadisticas.html")