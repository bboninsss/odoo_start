# -*- coding: utf-8 -*-
# from odoo import http


# class Galleria(http.Controller):
#     @http.route('/galleria/galleria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/galleria/galleria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('galleria.listing', {
#             'root': '/galleria/galleria',
#             'objects': http.request.env['galleria.galleria'].search([]),
#         })

#     @http.route('/galleria/galleria/objects/<model("galleria.galleria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('galleria.object', {
#             'object': obj
#         })
