# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmKpiReport(models.Model):
    _name = 'crm.kpi.report'
    _description = 'CRM KPI REPORT'
    _order = 'id desc'

    team_id = fields.Many2one(comodel_name="crm.team", string="Team")
    user_ids = fields.Many2many(comodel_name="res.users", string="User", required=True)
    activity_type_ids = fields.Many2many(comodel_name="mail.activity.type", string="Activity Type", required=True)
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
