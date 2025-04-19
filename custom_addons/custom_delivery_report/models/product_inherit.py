from odoo import models, fields

class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    cartoon_capacity = fields.Integer(string="Cartoon Capacity")
