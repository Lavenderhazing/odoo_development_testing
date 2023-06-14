# -*- coding: utf-8 -*-
# from odoo import http


# class NewModules(http.Controller):
#     @http.route('/new_modules/new_modules', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_modules/new_modules/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_modules.listing', {
#             'root': '/new_modules/new_modules',
#             'objects': http.request.env['new_modules.new_modules'].search([]),
#         })

#     @http.route('/new_modules/new_modules/objects/<model("new_modules.new_modules"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_modules.object', {
#             'object': obj
#         })
