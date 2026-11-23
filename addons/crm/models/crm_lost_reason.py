# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmLostReason(models.Model):
    _name = 'crm.lost.reason'
    _description = 'CRM LOST REASON'
    _order = 'id desc'

    name = fields.Char(string="Description", required=True)
    active = fields.Boolean(string="Active")
    leads_count = fields.Integer(string="Leads Count", readonly=True)
