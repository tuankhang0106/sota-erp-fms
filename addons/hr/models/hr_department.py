# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrDepartment(models.Model):
    _name = 'hr.department'
    _description = 'HR DEPARTMENT'
    _order = 'id desc'

    message_is_follower = fields.Boolean(string="Is Follower", readonly=True)
    message_follower_ids = fields.One2many(comodel_name="mail.followers", inverse_name='parent_id', string="Followers")
    message_partner_ids = fields.Many2many(comodel_name="res.partner", string="Followers (Partners)")
    message_ids = fields.One2many(comodel_name="mail.message", inverse_name='parent_id', string="Messages")
    has_message = fields.Boolean(string="Has Message", readonly=True)
    message_needaction = fields.Boolean(string="Action Needed", readonly=True, help="If checked, new messages require your attention.")
    message_needaction_counter = fields.Integer(string="Number of Actions", readonly=True, help="Number of messages requiring action")
    message_has_error = fields.Boolean(string="Message Delivery error", readonly=True, help="If checked, some messages have a delivery error.")
    message_has_error_counter = fields.Integer(string="Number of errors", readonly=True, help="Number of messages with delivery error")
    message_attachment_count = fields.Integer(string="Attachment Count", readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name="ir.attachment", string="Main Attachment")
    website_message_ids = fields.One2many(comodel_name="mail.message", inverse_name='parent_id', string="Website Messages", help="Website communication history")
    message_has_sms_error = fields.Boolean(string="SMS Delivery error", readonly=True, help="If checked, some messages have a delivery error.")
    name = fields.Char(string="Department Name", required=True)
    complete_name = fields.Char(string="Complete Name", readonly=True)
    active = fields.Boolean(string="Active")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    parent_id = fields.Many2one(comodel_name="hr.department", string="Parent Department")
    child_ids = fields.One2many(comodel_name="hr.department", inverse_name='parent_id', string="Child Departments")
    manager_id = fields.Many2one(comodel_name="hr.employee", string="Manager")
    member_ids = fields.One2many(comodel_name="hr.employee", inverse_name='parent_id', string="Members", readonly=True)
    total_employee = fields.Integer(string="Total Employee", readonly=True)
    jobs_ids = fields.One2many(comodel_name="hr.job", inverse_name='parent_id', string="Jobs")
    plan_ids = fields.One2many(comodel_name="hr.plan", inverse_name='parent_id', string="Plan")
    plans_count = fields.Integer(string="Plans Count", readonly=True)
    note = fields.Text(string="Note")
    color = fields.Integer(string="Color Index")
    parent_path = fields.Char(string="Parent Path")
    master_department_id = fields.Many2one(comodel_name="hr.department", string="Master Department", readonly=True)
    manager_ids = fields.Many2many(comodel_name="hr.employee", string="Superiors", readonly=True, help="Direct and indirect managers")
    recursive_child_ids = fields.Many2many(comodel_name="hr.department", string="Recursive Child Departments", readonly=True, help="Direct and Indirect Child Departments")
    expense_sheets_to_approve_count = fields.Integer(string="Expenses Reports to Approve", readonly=True)
    account_expense_id = fields.Many2one(comodel_name="account.account", string="Expense Account", help="Default Expense Account that will be used for encoding the department expenses into general accounting system (e.g. employee payroll expenses).")
    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", help="Default analytic account to be used for encoding analytic items related to payslips of this contract when no analytic account defined on the salary rules that concern.")
    analytic_distribution_model_ids = fields.Many2many(comodel_name="account.analytic.distribution.model", string="Analytic Distribution Models")
