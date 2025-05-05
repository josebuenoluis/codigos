from models.plantas_model import Plantas
from models.asistentes_model import Asistentes
from models.asistencias_model import Asistencias
from models.habitaciones_model import Habitaciones
from models.camas_model import Camas
from models.db import db
from sqlalchemy import func

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
    """Funcion para obtener las asistencias atendidas de un asistente"""
    resultado = (
    db.session.query(
        Asistentes.dni,
        Asistentes.nombre,
        Asistentes.planta_fk,
        func.count(Asistencias.id).label("conteo_asistencias")
    ).join(Asistencias, Asistentes.dni == Asistencias.asistente_fk)
        .group_by(Asistentes.dni, Asistentes.nombre, Asistentes.planta_fk)
        .all()
    )
    return resultado

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
    asistencias_atendidas = Asistencias.query.join(Habitaciones).join(Camas).filter(
        Habitaciones.planta_fk==n_planta,
        Asistencias.estado=="atendida"
    ).count()
    asistencias_atendidas = Asistencias.query.filter(Asistencias.estado=="atendida").count()
    return {"asistencias_atendidas":asistencias_atendidas,"asistencias_pendientes":asistencias_pendientes}
