# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountryGroup(models.Model):
    _name = 'res.country.group'
    _description = 'RES COUNTRY GROUP'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    country_ids = fields.Many2many(comodel_name="res.country", string="Countries")
    pricelist_ids = fields.Many2many(comodel_name="product.pricelist", string="Pricelists")
