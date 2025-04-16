# -*- coding: utf-8 -*-
# from odoo import http


# class SalesPortal(http.Controller):
#     @http.route('/sales_portal/sales_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_portal/sales_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_portal.listing', {
#             'root': '/sales_portal/sales_portal',
#             'objects': http.request.env['sales_portal.sales_portal'].search([]),
#         })

#     @http.route('/sales_portal/sales_portal/objects/<model("sales_portal.sales_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_portal.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/sales_portal', type='http', auth='public', website=True)
    def hello_world(self, **kw):
        # return "<h1>Hello from my custom controller! I am a developer , BDcalling</h1>"
         return request.render('sales_portal.sales_template', {})


    @http.route('/sales/order/form/', type='http', auth="public", website=True)
    def sales_order(self, **kw):

        products = request.env['product.product'].sudo().search([])
        return request.render('sales_portal.sales_form_template', {
            'products':products,
        })


    @http.route('/sales/submit', type='http', auth='public', methods=['POST'], website=True)
    def sales_submit(self, **post):
        customer_name = post.get('customer_name')
        email = post.get('email')
        product_name = post.get('product_id')
        quantity = int(post.get('quantity', 1))

        # Find customer or create a contact
        customer = request.env['res.partner'].sudo().search([('name', '=', customer_name)], limit=1)
        if not customer:
            customer = request.env['res.partner'].sudo().create({
                'name': customer_name,
                 'email': email,
            })

        # Find product
        product = request.env['product.product'].sudo().search([('name', 'ilike', product_name)], limit=1)
        if not product:
            return "Product not found."

        # Create sales order
        sale_order = request.env['sale.order'].sudo().create({
            'partner_id': customer.id,
        })

        # Add order line
        request.env['sale.order.line'].sudo().create({
            'order_id': sale_order.id,
            'product_id': product.id,
            'product_uom_qty': quantity,
            'price_unit': product.lst_price,
            'name': product.name,
        })

        return request.render('sales_portal.sales_order_success', {
            'sale_order': sale_order
        })
