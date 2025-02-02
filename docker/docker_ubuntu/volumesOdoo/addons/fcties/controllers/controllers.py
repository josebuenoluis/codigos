# -*- coding: utf-8 -*-
# from odoo import http


# class Fcties(http.Controller):
#     @http.route('/fcties/fcties', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fcties/fcties/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fcties.listing', {
#             'root': '/fcties/fcties',
#             'objects': http.request.env['fcties.fcties'].search([]),
#         })

#     @http.route('/fcties/fcties/objects/<model("fcties.fcties"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fcties.object', {
#             'object': obj
#         })

