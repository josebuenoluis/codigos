# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    name = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean()
    realizada = fields.Boolean()

    # @api.depends('prioridad')
    #  #Funcion para calcular el valor de urgente
    # def _value_urgente(self):
    #     #Para cada registro
    #     for record in self:
    #     #Si la prioridad es mayor que 10, se considera urgente, en otro caso no
    #     # lo es
    #         if record.prioridad > 10:
    #             record.urgente = True
    #         else:
    #             record.urgente = False