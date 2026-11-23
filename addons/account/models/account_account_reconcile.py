# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountAccountReconcile(models.Model):
    _name = 'account.account.reconcile'
    _description = 'ACCOUNT ACCOUNT RECONCILE'
    _order = 'id desc'

    reconcile_data_info = fields.Char(string="Reconcile Data Info")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    add_account_move_line_id = fields.Many2one(comodel_name="account.move.line", string="Add Account Move Line")
    manual_reference = fields.Char(string="Manual Reference")
    manual_delete = fields.Boolean(string="Manual Delete")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", readonly=True)
    foreign_currency_id = fields.Many2one(comodel_name="res.currency", string="Foreign Currency")
    company_currency_id = fields.Many2one(comodel_name="res.currency", string="Company Currency", readonly=True)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner", readonly=True)
    account_id = fields.Many2one(comodel_name="account.account", string="Account", readonly=True)
    name = fields.Char(string="Name", readonly=True)
    is_reconciled = fields.Boolean(string="Is Reconciled", readonly=True)
    active = fields.Boolean(string="Active")
