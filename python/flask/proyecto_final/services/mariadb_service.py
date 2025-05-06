from models.plantas_model import Plantas
from models.asistentes_model import Asistentes
from models.asistencias_model import Asistencias
from models.habitaciones_model import Habitaciones
from models.camas_model import Camas
from models.db import db
from sqlalchemy import func,extract
from datetime import datetime

def obtener_plantas() -> list[Plantas]:
    """"Funcion para obtener todas las plantas de la base de datos"""
    plantas = Plantas.query.all()
    return plantas

def obtener_asistentes() -> list[Asistentes]:
    """Funcion para obtener todos los asistentes de la base de datos"""
    asistentes = Asistentes.query.all()
    return asistentes

def crear_asistente(asistente_data:dict) -> tuple[bool, list[str]]:
    """Funcion para crear un asistente en la base de datos"""
    try:
        valido = False
        mensajes_error = validar_campos_asistente(asistente_data)
        if len(mensajes_error) == 0:
            asistente = Asistentes(dni=asistente_data["nif"], nombre=asistente_data["nombre"], 
            telefono=int(asistente_data["telefono"]), codigo=asistente_data["codigo"],
            planta_fk=int(asistente_data["planta"]))
            db.session.add(asistente)
            db.session.commit()
            valido = True
        print("Mensajes de error: ", mensajes_error)
        return valido, mensajes_error
    except Exception as e:
        print("Mensajes de error en EXCEPTION: ", e)
        db.session.rollback()
        return False,[]

def validar_campos_asistente(asistente_data:dict) -> list[str]:
    """Funcion para validar los campos del asistente"""
    mensajes_error = []
    if Asistentes.query.filter_by(dni=asistente_data["nif"]).first() is not None:
        mensajes_error.append("El dni ya existe")
    if Asistentes.query.filter_by(telefono=asistente_data["telefono"]).first() is not None:
        mensajes_error.append("El telefono ya existe")
    if Asistentes.query.filter_by(codigo=asistente_data["codigo"]).first() is not None:     
        mensajes_error.append("El codigo ya existe")
    if Plantas.query.filter_by(numero=asistente_data["planta"]).first() is None:
        mensajes_error.append("La planta no existe")   
    return mensajes_error

def modificar_asistentes(asistentes_data:dict) -> bool:
    """Funcion para modificar multiples asistentes"""
    try:
        for asistente in asistentes_data:
            asistente_db = Asistentes.query.filter_by(dni=asistente["nif"]).first()
            if asistente_db is not None:
                asistente_db.nombre = asistente["nombre"]
                asistente_db.telefono = int(asistente["telefono"])
                asistente_db.codigo = asistente["codigo"]
                asistente_db.planta_fk = int(asistente["planta"]) 
                db.session.commit()
        return True
    except Exception as e:
        print("Mensajes de error en EXCEPTION: ", e)
        db.session.rollback()
        return False
    
def eliminar_asistentes(nifs_data:list) -> bool:
    """Funcion para eliminar multiples asistentes"""
    try:
        for nif in nifs_data:
            asistente_db = Asistentes.query.filter_by(dni=nif).first()
            if asistente_db is not None:
                db.session.delete(asistente_db)
                db.session.commit()
        return True
    except Exception as e:
        print("Mensajes de error en EXCEPTION: ", e)
        db.session.rollback()
        return False


def obtener_asistentes_por_planta(planta:int) -> list[Asistentes]:
    """Funcion para obtener todos los asistentes de una planta"""
    asistentes = Asistentes.query.filter_by(planta_fk=planta).all()
    return asistentes

def asistencias_atendidas_asistente() -> list[Asistencias]:
    """Funcion para obtener las asistencias atendidas por asitente"""
    resultado = (
    db.session.query(
        Asistentes.dni,
        Asistentes.nombre,
        Asistentes.planta_fk,
        func.count(Asistencias.id).label("conteo_asistencias")
    ).join(Asistencias, Asistentes.dni == Asistencias.asistente_fk)
        .group_by(Asistentes.dni, Asistentes.nombre, Asistentes.planta_fk)
        .filter(Asistencias.estado=="atendida")
        .all()
    )
    resultado_dict = [
        {
            "dni":consulta_asistencia[0],
            "nombre":consulta_asistencia[1],
            "planta":consulta_asistencia[2],
            "asistencias_atendidas":consulta_asistencia[3]

        } for consulta_asistencia in resultado
    ]
    return resultado_dict

def asistencias_atendidas_asistente_planta(n_planta) -> list[Asistencias]:
    """Funcion para obtener las asistencias atendidas por asitente por planta"""
    resultado = (
    db.session.query(
        Asistentes.dni,
        Asistentes.nombre,
        Asistentes.planta_fk,
        func.count(Asistencias.id).label("conteo_asistencias")
    ).join(Asistencias, Asistentes.dni == Asistencias.asistente_fk)
        .group_by(Asistentes.dni, Asistentes.nombre, Asistentes.planta_fk)
        .filter(Asistencias.estado=="atendida",Asistentes.planta_fk==n_planta)
        .all()
    )
    resultado_dict = [
        {
            "dni":consulta_asistencia[0],
            "nombre":consulta_asistencia[1],
            "planta":consulta_asistencia[2],
            "asistencias_atendidas":consulta_asistencia[3]

        } for consulta_asistencia in resultado
    ]
    return resultado_dict

def obtener_asistencias_planta(planta:int) -> list[Asistencias]:
    """Funcion para obtener todas las asistencias de una planta"""
    asistencias = Asistencias.query.join(Habitaciones).join(Camas).filter(Habitaciones.planta_fk==planta).all()
    return asistencias

def obtener_asistencias() -> list[Asistencias]:
    """Funcion para obtener todas las asistencias"""
    asistencias = Asistencias.query.all()
    return asistencias

def conteo_asistencias() -> dict:
    """Funcion para devolver el numero de asistencias
    atendidas y no atendidas"""
    asistencias_pendientes = Asistencias.query.filter(Asistencias.estado=="pendiente").count()
    asistencias_atendidas = Asistencias.query.filter(Asistencias.estado=="atendida").count()
    return {"asistencias_atendidas":asistencias_atendidas,"asistencias_pendientes":asistencias_pendientes}

def conteo_asistencias_planta(n_planta:int) -> dict:
    """Funcion para devolver el numero de asistencias
    atendidas y no atendidas por planta"""
    asistencias_pendientes = Asistencias.query.join(Habitaciones).join(Camas).filter(
        Habitaciones.planta_fk==n_planta,
        Asistencias.estado=="pendiente"
    ).count()
    asistencias_atendidas = Asistencias.query.join(Habitaciones).filter(
        Habitaciones.planta_fk==n_planta,
        Asistencias.estado=="atendida"
    ).count()
    # asistencias_atendidas = Asistencias.query.filter(Asistencias.estado=="atendida").count()
    return {"asistencias_atendidas":asistencias_atendidas,"asistencias_pendientes":asistencias_pendientes}

def cargarPlantas():
    try:
        for i in range(1,6):
            planta = Plantas(numero=i)
            db.session.add(planta)
        db.session.commit()
    except Exception as e:
        print("Error en plantas",e)

def cargarHabitaciones():
    try:
        contador = 0
        for planta in range(1,6):
            for habitacion in range(1,11):
                contador += 1
                objeto = Habitaciones(numero=contador,planta_fk=planta)
                db.session.add(objeto)
        print("Guardando")
        db.session.commit()
    except Exception as e:
        print("Error al guardar habitaciones: ",e)
        db.session.rollback()


def cargarCamas():
    try:
        habitaciones = Habitaciones.query.all()
        for habitacion in habitaciones:
            objeto = Camas(nombre="a",habitacion_fk=habitacion.numero)
            objeto2 = Camas(nombre="b",habitacion_fk=habitacion.numero)
            db.session.add(objeto)
            db.session.add(objeto2)
        print("Guardando camas")
        db.session.commit()
    except Exception as e:
        print("Error al guardar camas: ",e)
        db.session.rollback()

def cargarAsistencias():
    try:
        habitaciones = Habitaciones.query.all()
        for habitacion in habitaciones:
            camas = Camas.query.filter_by(habitacion_fk=habitacion.numero).all()
            for cama in camas:
                objeto = Asistencias(habitacion_fk=habitacion.numero, cama_fk=cama.id)
                db.session.add(objeto)
        print("Guardando asistencias")
        db.session.commit()
    except Exception as e:
        print("Error al guardar asistencias: ",e)
        db.session.rollback()

def obtener_historico(desde="",hasta="") -> list[dict]:
    """Funcion para obtener asistencias por mes y anio"""
    if desde != "" and hasta != "":
        print(desde,hasta)
        desde = datetime.strptime(desde,"%Y-%m-%d")
        hasta = datetime.strptime(hasta,"%Y-%m-%d")
        asistencias_historico = db.session.query(
            extract('year',Asistencias.fecha_llamada).label('anio'),
            extract('month',Asistencias.fecha_llamada).label('mes'),
            func.count(Asistencias.id).label("conteo_asistencias")
        ).filter(
            Asistencias.fecha_llamada >= desde, Asistencias.fecha_llamada <= hasta,
        ).group_by('mes','anio').order_by('mes','anio').all()
    else:    
        asistencias_historico = db.session.query(
            extract('year',Asistencias.fecha_llamada).label('anio'),
            extract('month',Asistencias.fecha_llamada).label('mes'),
            func.count(Asistencias.id).label("conteo_asistencias")
        ).group_by('mes','anio').order_by('mes','anio').all()
    resultado_dict = [
        {
            "anio":asistencia[0],
            "mes":asistencia[1],
            "total_asistencias":asistencia[2]
        } for asistencia in asistencias_historico
    ]
    return resultado_dict

def obtener_conteo_asistencias_planta() -> dict:
    """Funcion para devolver el numero de asistencias
    atendidas y no atendidas por planta"""
    asistencias_por_planta = db.session.query(
        Habitaciones.planta_fk,
        func.count(Asistencias.id).label("total_asistencias")
    ).join(Habitaciones, Asistencias.habitacion_fk == Habitaciones.numero).filter(
        Asistencias.estado=="atendida"
    ).group_by(Habitaciones.planta_fk).all()

    asistencias_atendidas_dict = [
        {
            "planta": asistencia[0],
            "total_asistencias": asistencia[1]
        } for asistencia in asistencias_por_planta
    ]
    return {"asistencias_atendidas":asistencias_atendidas_dict}

def obtener_llamados_habitaciones() -> list[Asistencias]:
    """Funcion para obtener las 10 habitaciones
    con mas llamados"""
    habitaciones = db.session.query(
        Asistencias.habitacion_fk,
        func.count(Asistencias.id).label("conteo_llamadas")
    ).group_by(Asistencias.habitacion_fk).order_by(func.count(Asistencias.id).desc()).limit(10).all()
    print(habitaciones)
    return habitaciones