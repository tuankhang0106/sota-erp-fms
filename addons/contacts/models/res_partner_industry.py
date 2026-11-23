# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerIndustry(models.Model):
    _name = 'res.partner.industry'
    _description = 'RES PARTNER INDUSTRY'
    _order = 'id desc'

    name = fields.Char(string="Name")
    full_name = fields.Char(string="Full Name")
    active = fields.Boolean(string="Active")
