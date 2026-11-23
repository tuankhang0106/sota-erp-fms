# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CalendarEventType(models.Model):
    _name = 'calendar.event.type'
    _description = 'CALENDAR EVENT TYPE'

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
