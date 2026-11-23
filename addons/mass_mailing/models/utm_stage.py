# -*- coding: utf-8 -*-
from odoo import models, fields, api

class UtmStage(models.Model):
    _name = 'utm.stage'
    _description = 'UTM STAGE'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(string="Sequence")
