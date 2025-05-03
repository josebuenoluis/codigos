from models.plantas_model import Plantas
from models.asistentes_model import Asistentes
from models.db import db

def obtener_plantas() -> list[Plantas]:
    """"Funcion para obtener todas las plantas de la base de datos"""
    plantas = Plantas.query.all()
    return plantas

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
        print("Mensajes de error: ", e)
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
    if Asistentes.query.filter_by(planta_fk=asistente_data["planta"]).first() is None:
        mensajes_error.append("La planta no existe")   
    return mensajes_error




