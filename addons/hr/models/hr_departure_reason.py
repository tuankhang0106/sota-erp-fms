# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrDepartureReason(models.Model):
    _name = 'hr.departure.reason'
    _description = 'HR DEPARTURE REASON'
    _order = 'id desc'

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Reason", required=True)
