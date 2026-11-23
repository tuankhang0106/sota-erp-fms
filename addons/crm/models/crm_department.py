# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmDepartment(models.Model):
    _name = 'crm.department'
    _description = 'CRM DEPARTMENT'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    user_id = fields.Many2one(comodel_name="res.users", string="Manager")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    team_ids = fields.One2many(comodel_name="crm.team", inverse_name='parent_id', string="Sales Team")
    team_count = fields.Integer(string="Team Count", readonly=True)
