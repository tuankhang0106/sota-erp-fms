# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SpreadsheetDashboardGroup(models.Model):
    _name = 'spreadsheet.dashboard.group'
    _description = 'SPREADSHEET DASHBOARD GROUP'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    dashboard_ids = fields.One2many(comodel_name="spreadsheet.dashboard", inverse_name='parent_id', string="Dashboard")
    sequence = fields.Integer(string="Sequence")
