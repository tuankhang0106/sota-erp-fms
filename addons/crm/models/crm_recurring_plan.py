# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmRecurringPlan(models.Model):
    _name = 'crm.recurring.plan'
    _description = 'CRM RECURRING PLAN'
    _order = 'id desc'

    name = fields.Char(string="Plan Name", required=True)
    number_of_months = fields.Integer(string="# Months", required=True)
    active = fields.Boolean(string="Active")
    sequence = fields.Integer(string="Sequence")
