# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo2(http.Controller):
#     @http.route('/ejemplo2/ejemplo2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo2/ejemplo2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo2.listing', {
#             'root': '/ejemplo2/ejemplo2',
#             'objects': http.request.env['ejemplo2.ejemplo2'].search([]),
#         })

#     @http.route('/ejemplo2/ejemplo2/objects/<model("ejemplo2.ejemplo2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo2.object', {
#             'object': obj
#         })

