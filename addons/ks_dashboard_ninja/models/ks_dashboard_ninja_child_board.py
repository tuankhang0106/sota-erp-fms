# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ks_dashboard_ninjaChild_board(models.Model):
    _name = 'ks_dashboard_ninja.child_board'
    _description = 'KS_DASHBOARD_NINJA CHILD_BOARD'
    _order = 'id desc'

    name = fields.Char(string="Name")
    ks_dashboard_ninja_id = fields.Many2one(comodel_name="ks_dashboard_ninja.board", string="Select Dashboard")
    ks_gridstack_config = fields.Char(string="Item Configurations")
    ks_active = fields.Boolean(string="Is Selected")
    ks_dashboard_menu_name = fields.Char(string="Menu Name", readonly=True)
    board_type = fields.Selection(selection=[["default","Default"],["child","Child"]], string="Board Type")
    company_id = fields.Many2one(comodel_name="res.company", string="Company", required=True)
