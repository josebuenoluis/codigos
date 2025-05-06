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
@api.route("/api/asistentes/estadisticas/<int:n_planta>", methods=["GET"])
def obtener_asistentes_estadisticas(n_planta:int=0):
    if n_planta != 0:
        asistentes_asistencias = db_service.asistencias_atendidas_asistente_planta(n_planta)
    else:
        asistentes_asistencias = db_service.asistencias_atendidas_asistente()
    return asistentes_asistencias

@api.route("/api/asistencias",methods=["GET"])
@api.route("/api/asistencias/<int:n_planta>",methods=["GET"])
def obtener_asistencias(n_planta:int=0):
    if n_planta != 0:
        asistencias = db_service.obtener_asistencias_planta(n_planta)
    else:
        asistencias = db_service.obtener_asistencias()
    print("Asistencias: ", asistencias)
    return jsonify([asistencia.to_dict() for asistencia in asistencias])

@api.route("/api/asistencias/plantas",methods=["GET"])
def obtener_asistencias_plantas():
    asistencias = db_service.obtener_conteo_asistencias_planta()
    return asistencias

@api.route("/api/asistencias/conteo",methods=["GET"])
@api.route("/api/asistencias/conteo/<int:n_planta>",methods=["GET"])
def asistencias_conteo(n_planta:int=0):
    if n_planta != 0:
        conteo_asistencias = db_service.conteo_asistencias_planta(n_planta)
    else:
        conteo_asistencias = db_service.conteo_asistencias()
    return conteo_asistencias

@api.route("/api/asistencias/historico",methods=["GET"])
def asistencias_historico():
    desde = request.args.get("desde","")
    hasta = request.args.get("hasta","")
    if desde != "" and hasta != "":
        asistencias_historico = db_service.obtener_historico(desde,hasta)
        pass
    else:
        asistencias_historico = db_service.obtener_historico()
    return asistencias_historico

@api.route("/api/habitaciones/asistencias/conteo")
def obtener_conteo_llamadas_habitaciones():
    habitaciones_asistencias = db_service.obtener_llamados_habitaciones()
    resultado_dict = [
        {
            "habitacion":habitacion[0],
            "conteo_llamadas":habitacion[1]
        } for habitacion in habitaciones_asistencias
    ]
    return {"success":True}