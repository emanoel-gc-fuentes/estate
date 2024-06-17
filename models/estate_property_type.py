from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'estate.property.type'
    
    name = fields.Char('name', required=True)