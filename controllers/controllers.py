# -*- coding: utf-8 -*-
# from odoo import http


# class TestCicd(http.Controller):
#     @http.route('/test_cicd/test_cicd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_cicd/test_cicd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_cicd.listing', {
#             'root': '/test_cicd/test_cicd',
#             'objects': http.request.env['test_cicd.test_cicd'].search([]),
#         })

#     @http.route('/test_cicd/test_cicd/objects/<model("test_cicd.test_cicd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_cicd.object', {
#             'object': obj
#         })
