from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate.property.offer"

    price = fields.Float('price')
    
    status = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused'),
    ], 'status')

    partner_id = fields.Many2one('res.partner', required=True)

    property_id = fields.Many2one('estate.property', required=True)