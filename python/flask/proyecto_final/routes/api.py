from flask import jsonify,Blueprint,request
from services import mariadb_service as db_service
api = Blueprint("api",__name__)

@api.route("/api/plantas", methods=["GET"])
def obtener_plantas():
    plantas = db_service.obtener_plantas()
    return jsonify([planta.to_dict() for planta in plantas])

@api.route("/api/asistentes", methods=["GET"])
def obtener_asistentes():
    asistentes = db_service.obtener_asistentes()
    return jsonify([asistente.to_dict() for asistente in asistentes])

@api.route("/api/asistentes/estadisticas", methods=["GET"])
def obtener_asistentes_estadisticas():
    asistentes_asistencias = db_service.asistencias_atendidas_asistente()
    return jsonify([asistente.to_dict() for asistente in asistentes_asistencias])

@api.route("/api/asistencias",methods=["GET"])
@api.route("/api/asistencias/<int:n_planta>",methods=["GET"])
def obtener_asistencias(n_planta:int=0):
    if n_planta != 0:
        asistencias = db_service.obtener_asistencias_planta(n_planta)
    else:
        asistencias = db_service.obtener_asistencias()
    print("Asistencias: ", asistencias)
    return jsonify([asistencia.to_dict() for asistencia in asistencias])

@api.route("/api/asistencias/conteo",methods=["GET"])
@api.route("/api/asistencias/conteo/<int:n_planta>",methods=["GET"])
def asistencias_conteo(n_planta:int=0):
    if n_planta != 0:
        conteo_asistencias = db_service.conteo_asistencias_planta(n_planta)
    else:
        conteo_asistencias = db_service.conteo_asistencias()
    return conteo_asistencias
