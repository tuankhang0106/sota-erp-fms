# -*- coding: utf-8 -*-
from odoo import models, fields, api

class UtmTag(models.Model):
    _name = 'utm.tag'
    _description = 'UTM TAG'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color Index", help="Tag color. No color means no display in kanban to distinguish internal tags from public categorization tags.")
