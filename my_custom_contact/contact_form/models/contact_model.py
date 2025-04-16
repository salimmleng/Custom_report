from odoo import models, fields

class ContactMessage(models.Model):
    _name = 'contact.message'
    _description = 'Contact Form Messages'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    message = fields.Text(string="Message", required=True)


