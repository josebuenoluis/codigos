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
        valido,mensajes_error = db_service.crear_asistente(asistente_data)
        print("Mensajes de error en ruta asistentes: ", mensajes_error,valido)
        if valido:
            return jsonify({'success': True, 'message': ["Asistente creado correctamente"]})
        else:
            return jsonify({'success': False, 'message': mensajes_error})


@asistentes.route("/asistentes/modificar", methods=["GET","PUT","DELETE"])
def modificar_asistente():
    if request.method == "GET":
        plantas = db_service.obtener_plantas()
        asistentes = db_service.obtener_asistentes()
        return render_template("asistentes-modificar.html",plantas=plantas,asistentes=asistentes)
    elif request.method == "DELETE":
        data = request.get_json()
        print("Data: ",data)
        valido = db_service.eliminar_asistentes 
        (data)
        if valido:
            return jsonify({'success': True, 'message': ["Asistentes eliminados correctamente"]})
        else:
            return jsonify({'success': False, 'message': ["Error al eliminar asistentes"]})
    else:
        data = request.get_json()
        print("Data: ",data)
        valido = db_service.modificar_asistentes(data)
        if valido:
            return jsonify({'success': True, 'message': ["Asistentes modificado correctamente"]})
        else:
            return jsonify({'success': False, 'message': ["Error al modificar asistentes"]})

@asistentes.route("/asistentes/estadisticas", methods=["GET"])
def estadisticas_asistente():
    asistentes_asistencias = db_service.asistencias_atendidas_asistente()
    plantas = db_service.obtener_plantas()
    return render_template("asistentes-estadisticas.html",
    asistentes_asistencias=asistentes_asistencias,plantas=plantas)

