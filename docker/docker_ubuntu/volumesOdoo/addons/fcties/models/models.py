# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# odoo.exceptions.ValidationError


class Alumno(models.Model):
    _name = 'alumnos.alumno'
    _description = 'Modelo de alumno'
    nombre = fields.Char(string="Nombre",required=True)  # (Obligatorio)
    apellidos = fields.Char(string="Apellido",required=True) # Apellidos (obligatorio).
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True) #Fecha de nacimiento (obligatorio).
    curso_academico = fields.Char(string="Curso Académico",required=True) # Curso académico (formato 24/25).
    correo_electronico =  fields.Char(string="Correo electrónico")  #(opcional).
    telefono = fields.Char(string="Teléfono")  #(opcional).
    ciclo_formativo = fields.Selection([
        ("DAM","Desarrollo de Aplicaciones Multiplataforma"),
        ("DAW","Desarrollo de Aplicaciones Web"),
        ("ASIR","Administración de Sistemas Informáticos en Red")
        ],string="Ciclo Formativo",required=True) #(puede ser: DAM, DAW y ASIR, obligatorio).
    periodo_practica = fields.Selection([
        ("abril","Abril"),
        ("septiembre","Septiembre")
        ],string="Periodo de Práctica",required=True) # Periodo de práctica (abril o septiembre, obligatorio).
    nota_media = fields.Float(string="Nota Media",required=True) # Nota media (obligatorio).
    nota_media_texto = fields.Text(string="Nota media en texto",compute="_compute_calcular_media",store=True)
    empresa_id = fields.Many2one("empresas.empresa",string="Empresa de practicas")


    @api.onchange("curso_academico")
    def _validar_formato(self):
        for record in self:
            if record.curso_academico:
                if not (len(record.curso_academico.split("/")) == 2 and record.curso_academico.split("/")[0].isdigit()\
                         and record.curso_academico.split("/")[1].isdigit() and len(record.curso_academico.split("/")[0])==2\
                            and len(record.curso_academico.split("/")[1])==2): 
                    raise ValidationError("El formato debe ser asi 24/25")
                

    @api.onchange("correo_electronico")
    def _validar_correo(self):
        for record in self:
            if record.correo_electronico:
                if not (len(record.correo_electronico.split("@")) == 2 and\
                    len(record.correo_electronico.split("@")[1].split(".")) == 2 and\
                    record.correo_electronico.split("@")[0] != "" and\
                    record.correo_electronico.split("@")[1].split(".")[0] != "" and \
                    record.correo_electronico.split("@")[1].split(".")[1].isalpha()):
                    raise ValidationError("El correo electrónico no es válido.")
                    

    @api.onchange("telefono")
    def _validar_telefono(self):
        for record in self:
            if record.telefono:
                if not (len(record.telefono) == 9 and record.telefono.isdigit()):  
                    raise ValidationError("El telefono ingresado no es valido.")

    # Nota media en formato texto (campo calculado como se indica más adelante).
    @api.depends("nota_media")
    def _compute_calcular_media(self):
        for record in self:
            if record.nota_media:
                if record.nota_media >= 9:
                    record.nota_media_texto = "Sobresaliente"
                elif record.nota_media >= 7:
                    record.nota_media_texto = "Notable"
                elif record.nota_media >= 5:
                    record.nota_media_texto = "Aprobado"
                else:
                    record.nota_media_texto = "Suspendido"
            else:
                record.nota_media_texto = "No hay nota"

class Empresa(models.Model):
    _name = 'empresas.empresa'
    _description = 'Modelo de empresa'
    _rec_name = "nombre"
    nombre = fields.Char(string="Nombre de empresa",required=True) # Nombre (obligatorio).
    persona_contacto = fields.Char(string="Persona de contacto",required=True) # Persona de contacto (obligatorio).
    telefono = fields.Char(string="Teléfono",required=True) # Teléfono de contacto (obligatorio).
    correo_electronico = fields.Char(string="Correo electrónico",required=True) # Correo electrónico (obligatorio).
    direccion = fields.Char(string="Dirección",required=True)   # Dirección (obligatorio).
    alumno_ids = fields.One2many("alumnos.alumno","empresa_id",string="Alumnos en practica")


    @api.onchange("correo_electronico")
    def _validar_correo(self):
        for record in self:
            if record.correo_electronico:
                if not (len(record.correo_electronico.split("@")) == 2 and\
                    len(record.correo_electronico.split("@")[1].split(".")) == 2 and\
                    record.correo_electronico.split("@")[0] != "" and\
                    record.correo_electronico.split("@")[1].split(".")[0] != "" and \
                    record.correo_electronico.split("@")[1].split(".")[1].isalpha()):
                    raise ValidationError("El correo electrónico no es válido.")
                    

    @api.onchange("telefono")
    def _validar_telefono(self):
        for record in self:
            if record.telefono:
                if not (len(record.telefono) == 9 and record.telefono.isdigit()):  
                    raise ValidationError("El telefono ingresado no es valido.")
