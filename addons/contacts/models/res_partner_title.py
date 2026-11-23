# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerTitle(models.Model):
    _name = 'res.partner.title'
    _description = 'RES PARTNER TITLE'
    _order = 'id desc'

    name = fields.Char(string="Title", required=True)
    shortcut = fields.Char(string="Abbreviation")
