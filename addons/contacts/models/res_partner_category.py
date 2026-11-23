# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerCategory(models.Model):
    _name = 'res.partner.category'
    _description = 'RES PARTNER CATEGORY'
    _order = 'id desc'

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color")
    parent_id = fields.Many2one(comodel_name="res.partner.category", string="Parent Category")
    child_ids = fields.One2many(comodel_name="res.partner.category", inverse_name='parent_id', string="Child Tags")
    active = fields.Boolean(string="Active", help="The active field allows you to hide the category without removing it.")
    parent_path = fields.Char(string="Parent Path")
    partner_ids = fields.Many2many(comodel_name="res.partner", string="Partners")
