# -*- coding: utf-8 -*-
# from odoo import http


# class CustomDeliveryReport(http.Controller):
#     @http.route('/custom_delivery_report/custom_delivery_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_delivery_report/custom_delivery_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_delivery_report.listing', {
#             'root': '/custom_delivery_report/custom_delivery_report',
#             'objects': http.request.env['custom_delivery_report.custom_delivery_report'].search([]),
#         })

#     @http.route('/custom_delivery_report/custom_delivery_report/objects/<model("custom_delivery_report.custom_delivery_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_delivery_report.object', {
#             'object': obj
#         })

