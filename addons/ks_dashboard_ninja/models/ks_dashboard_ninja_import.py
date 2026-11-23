# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ks_dashboard_ninjaImport(models.Model):
    _name = 'ks_dashboard_ninja.import'
    _description = 'KS_DASHBOARD_NINJA IMPORT'
    _order = 'id desc'

    ks_import_dashboard = fields.Binary(string="Upload Dashboard")
    ks_top_menu_id = fields.Many2one(comodel_name="ir.ui.menu", string="Show Under Menu", required=True)
