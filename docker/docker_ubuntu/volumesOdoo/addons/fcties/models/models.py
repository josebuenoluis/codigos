# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'alumnos.alumno'
    _description = 'alumnos.alumno'

    nombre = fields.Char()  # (Obligatorio)
    apellidos = fields.Char() # Apellidos (obligatorio).
    fecha_nacimiento = fields.Date() #Fecha de nacimiento (obligatorio).
    curso_academico = fields.Date() # Curso académico (formato 24/25).
    Correo_electrónico =  fields.Char()  #(opcional).
    telefono = fields.Integer()  #(opcional).
    #ciclo_formativo = fields.Selection([("dam","DAM"),("daw","DAW"),("asir","ASIR")]) #(puede ser: DAM, DAW y ASIR, obligatorio).
    #periodo_practica = fields.Date([("abril","abril"),("septiembre","septiembre")]) # Periodo de práctica (abril o septiembre, obligatorio).
    nota_media = fields.Float() # Nota media (obligatorio).


    # Nota media en formato texto (campo calculado como se indica más adelante).
    def calcularMedia(self):
        pass

class Empresa(models.Model):
    _name = 'empresas.empresa'
    _description = 'empresas.empresa'

    nombre = fields.Char() # Nombre (obligatorio).
    persona_contacto = fields.Char() # Persona de contacto (obligatorio).
    telefono = fields.Integer() # Teléfono de contacto (obligatorio).
    correo_electronico = fields.Char() # Correo electrónico (obligatorio).
    direccion = fields.Char()   # Dirección (obligatorio).