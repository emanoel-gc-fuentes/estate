from odoo import models, fields
import datetime

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate.property'

    # invisible="1" | Definir no arquivo xml;
    active = fields.Boolean('active', default=True)

    name = fields.Char('name', required=True, default='new')
    
    state = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')],
        required=True,
        copy=True,
        default='new',
        string='state')
    
    description = fields.Text('description')
    
    postcode = fields.Char('postcode')
    
    def _default_date(self):
        return fields.Date.today()
    
    date_availability = fields.Date('date availability', copy=False, default=_default_date)
    
    expected_price = fields.Float('expected price', required=True, copy=False)
    
    selling_price = fields.Float('selling price', readonly=True)
    
    bedrooms = fields.Integer('bedrooms', default=2)
    
    living_area = fields.Integer('living area')
    
    facades = fields.Integer('facades')
    
    garage = fields.Boolean('garage')
    
    garden = fields.Boolean('garden')
    
    garden_area = fields.Integer('garden area')
    
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('shouth', 'Shouth'),
        ('east', 'East'),
        ('west', 'West'),
    ], string='garden orientation')

    property_type_id = fields.Many2one('estate.property.type', string='property type')

    partner_id = fields.Many2one('res.partner', string='partner_id', copy=False)

    def _compute_user_id(self):
        for order in self:
            if order and not order.user_id:
                order.user_id = (order.create_uid)

    user_id = fields.Many2one('res.users', string='user_id', compute="_compute_user_id")
