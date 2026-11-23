# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _name = 'account.analytic.line'
    _description = 'ACCOUNT ANALYTIC LINE'
    _order = 'id desc'

    name = fields.Char(string="Description", required=True)
    date = fields.Date(string="Date", required=True)
    amount = fields.Monetary(string="Amount", required=True)
    unit_amount = fields.Float(string="Quantity")
    product_uom_id = fields.Many2one(comodel_name="uom.uom", string="Unit of Measure")
    product_uom_category_id = fields.Many2one(comodel_name="uom.category", string="UoM Category", readonly=True, help="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.")
    account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", required=True)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")
    user_id = fields.Many2one(comodel_name="res.users", string="User")
    company_id = fields.Many2one(comodel_name="res.company", string="Company", required=True, readonly=True)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", readonly=True)
    plan_id = fields.Many2one(comodel_name="account.analytic.plan", string="Plan", readonly=True)
    category = fields.Selection(selection=[["other","Other"],["invoice","Customer Invoice"],["vendor_bill","Vendor Bill"]], string="Category")
    product_id = fields.Many2one(comodel_name="product.product", string="Product")
    general_account_id = fields.Many2one(comodel_name="account.account", string="Financial Account")
    journal_id = fields.Many2one(comodel_name="account.journal", string="Financial Journal", readonly=True)
    move_line_id = fields.Many2one(comodel_name="account.move.line", string="Journal Item")
    code = fields.Char(string="Code")
    ref = fields.Char(string="Ref.")
    move_id = fields.Many2one(comodel_name="account.move", string="Journal Entry", readonly=True)
    move_type = fields.Selection(selection=[["entry","Journal Entry"],["out_invoice","Customer Invoice"],["out_refund","Customer Credit Note"],["in_invoice","Vendor Bill"],["in_refund","Vendor Credit Note"],["out_receipt","Sales Receipt"],["in_receipt","Purchase Receipt"]], string="Type", readonly=True)
    tag_ids = fields.Many2many(comodel_name="account.analytic.tag", string="Analytic Tags")
