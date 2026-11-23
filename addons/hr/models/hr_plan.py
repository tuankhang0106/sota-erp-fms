# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrPlan(models.Model):
    _name = 'hr.plan'
    _description = 'HR PLAN'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    department_id = fields.Many2one(comodel_name="hr.department", string="Department")
    plan_activity_type_ids = fields.One2many(comodel_name="hr.plan.activity.type", inverse_name='parent_id', string="Activities")
    active = fields.Boolean(string="Active")
    steps_count = fields.Integer(string="Steps Count", readonly=True)
