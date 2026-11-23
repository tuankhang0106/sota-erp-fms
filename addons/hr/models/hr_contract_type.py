# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrContractType(models.Model):
    _name = 'hr.contract.type'
    _description = 'HR CONTRACT TYPE'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(string="Sequence")
