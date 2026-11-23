# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerResource(models.Model):
    _name = 'res.partner.resource'
    _description = 'RES PARTNER RESOURCE'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
