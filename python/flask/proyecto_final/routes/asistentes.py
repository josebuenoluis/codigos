from flask import render_template,Blueprint,request,jsonify
from services import mariadb_service as db_service
from models.db import db
asistentes = Blueprint("asistentes",__name__)

@asistentes.route("/asistentes/crear", methods=["GET","POST"])
def crear_asistente():
    if request.method == "GET":
        plantas = db_service.obtener_plantas()
        return render_template("crear-asistente.html", plantas=plantas)
    else:
        data = request.get_json()
        print("Data: ",data)
        asistente_data = {
            "nif": data["nif"],
            "nombre": data["nombre"],
            "telefono": data["telefono"],
            "codigo": data["codigo"],
            "planta": data["planta"]
        }
        # plantas = db_service.obtener_plantas()
        valido,mensajes_error = db_service.crear_asistente(asistente_data)
        if valido:
            return jsonify({'success': True, 'message': 'Usuario registrado correctamente'})
        else:
            return jsonify({'success': False, 'message': mensajes_error})

@asistentes.route("/asistentes/modificar", methods=["GET"])
def modificar_asistente():
    return render_template("asistentes-modificar.html")

@asistentes.route("/asistentes/estadisticas", methods=["GET"])
def estadisticas_asistente():
    return render_template("asistentes-estadisticas.html")

