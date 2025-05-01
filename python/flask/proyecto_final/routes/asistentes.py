from flask import render_template,Blueprint

asistentes = Blueprint("asistentes",__name__)

@asistentes.route("/asistentes/crear", methods=["GET"])
def crear_asistente():
    return render_template("crear-asistente.html")