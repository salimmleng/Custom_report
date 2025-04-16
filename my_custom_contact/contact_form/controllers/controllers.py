# -*- coding: utf-8 -*-
# from odoo import http


# class ContactForm(http.Controller):
#     @http.route('/contact_form/contact_form', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_form/contact_form/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_form.listing', {
#             'root': '/contact_form/contact_form',
#             'objects': http.request.env['contact_form.contact_form'].search([]),
#         })

#     @http.route('/contact_form/contact_form/objects/<model("contact_form.contact_form"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_form.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/contact', type='http', auth='public', website=True)
    def contact_form(self, **kw):
         return request.render('contact_form.contact_form_template', {})

    @http.route('/contact/submit', type='http', auth='public', methods=['POST'], website=True)
    def submit_form(self, **post):
        name = post.get('name')
        email = post.get('email')
        message = post.get('message')

        print(name)
        print(email)
        print(message)

        customer = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
        })

        request.env['contact.message'].sudo().create({
            'name':name,
            'email':email,
            'message':message
        })

        print()

        return request.render('contact_form.contact_thank_you', {
            'name': name
        })


