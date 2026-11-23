# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ShActivityTags(models.Model):
    _name = 'sh.activity.tags'
    _description = 'SH ACTIVITY TAGS'

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color")
