# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrWorkLocation(models.Model):
    _name = 'hr.work.location'
    _description = 'HR WORK LOCATION'
    _order = 'id desc'

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Work Location", required=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", required=True)
    address_id = fields.Many2one(comodel_name="res.partner", string="Work Address", required=True)
    location_number = fields.Char(string="Location Number")
