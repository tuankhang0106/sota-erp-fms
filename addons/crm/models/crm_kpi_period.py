# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmKpiPeriod(models.Model):
    _name = 'crm.kpi.period'
    _description = 'CRM KPI PERIOD'
    _order = 'id desc'

    team_id = fields.Many2one(comodel_name="crm.team", string="Sales Team", required=True)
    crm_department_id = fields.Many2one(comodel_name="crm.department", string="Department", readonly=True)
    month = fields.Selection(selection=[["01","January"],["02","February"],["03","March"],["04","April"],["05","May"],["06","June"],["07","July"],["08","August"],["09","September"],["10","October"],["11","November"],["12","December"]], string="Month", required=True)
    year = fields.Integer(string="Year", required=True)
    name = fields.Char(string="Name", readonly=True)
    kpi_entries = fields.One2many(comodel_name="crm.kpi.entry", inverse_name='parent_id', string="KPI Entries")
    default_kpi_calling = fields.Integer(string="Default Calling")
    default_kpi_quotation_sent = fields.Integer(string="Default Quotation Sent")
    default_kpi_win_deal = fields.Integer(string="Default Win Deal")
    default_kpi_meeting = fields.Integer(string="Default Meeting")
