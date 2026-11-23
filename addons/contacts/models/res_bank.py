# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResBank(models.Model):
    _name = 'res.bank'
    _description = 'RES BANK'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    zip = fields.Char(string="Zip")
    city = fields.Char(string="City")
    state = fields.Many2one(comodel_name="res.country.state", string="Fed. State")
    country = fields.Many2one(comodel_name="res.country", string="Country")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    active = fields.Boolean(string="Active")
    bic = fields.Char(string="Bank Identifier Code", help="Sometimes called BIC or Swift.")
