# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ShActivityDynamicAction(models.Model):
    _name = 'sh.activity.dynamic.action'
    _description = 'SH ACTIVITY DYNAMIC ACTION'

    name = fields.Char(string="Action Name", required=True)
    model_id = fields.Many2one(comodel_name="ir.model", string="Applies To", required=True, help="The model this field belongs to")
    sh_group_ids = fields.Many2many(comodel_name="res.groups", string="Groups")
    action_id = fields.Many2one(comodel_name="ir.actions.act_window", string="Related Action")
