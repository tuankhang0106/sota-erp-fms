# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EmployeeAdvanceReconcileBatch(models.Model):
    _name = 'employee.advance.reconcile.batch'
    _description = 'EMPLOYEE ADVANCE RECONCILE BATCH'
    _order = 'id desc'

    date = fields.Date(string="Date", required=True)
    journal_id = fields.Many2one(comodel_name="account.journal", string="Employee Advance Journal", required=True)
    employee_domain_ids = fields.Many2many(comodel_name="hr.employee", string="Employee Domain", readonly=True, help="The technical field that stores the domain for employee_ids field")
    employee_ids = fields.Many2many(comodel_name="hr.employee", string="Employees")
