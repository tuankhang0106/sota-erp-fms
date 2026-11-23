# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ChangeLockDate(models.Model):
    _name = 'change.lock.date'
    _description = 'CHANGE LOCK DATE'
    _order = 'id desc'

    company_id = fields.Many2one(comodel_name="res.company", string="Company", required=True)
    period_lock_date = fields.Date(string="Journal Entries Lock Date", help="Prevent posting of journal entries in this period.")
    fiscalyear_lock_date = fields.Date(string="Lock Date for All Users", help="No users, including Advisers, can edit accounts prior to and inclusive of this date. Use it for fiscal year locking.")
    tax_lock_date = fields.Date(string="Tax Lock Date", help="No users can edit journal entries related to a tax prior and inclusive of this date.")
