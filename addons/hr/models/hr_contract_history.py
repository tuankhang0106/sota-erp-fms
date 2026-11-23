# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrContractHistory(models.Model):
    _name = 'hr.contract.history'
    _description = 'HR CONTRACT HISTORY'
    _order = 'id desc'

    contract_id = fields.Many2one(comodel_name="hr.contract", string="Contract", readonly=True)
    name = fields.Char(string="Contract Name", readonly=True)
    date_hired = fields.Date(string="Hire Date", readonly=True)
    date_start = fields.Date(string="Start Date", readonly=True)
    date_end = fields.Date(string="End Date", readonly=True)
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", readonly=True)
    active_employee = fields.Boolean(string="Active Employee", readonly=True)
    is_under_contract = fields.Boolean(string="Is Currently Under Contract", readonly=True)
    department_id = fields.Many2one(comodel_name="hr.department", string="Department", readonly=True)
    structure_type_id = fields.Many2one(comodel_name="hr.payroll.structure.type", string="Salary Structure Type", readonly=True)
    hr_responsible_id = fields.Many2one(comodel_name="res.users", string="HR Responsible", readonly=True)
    job_id = fields.Many2one(comodel_name="hr.job", string="Job Position", readonly=True)
    state = fields.Selection(selection=[["draft","New"],["open","Running"],["close","Expired"],["cancel","Cancelled"]], string="Status", readonly=True)
    resource_calendar_id = fields.Many2one(comodel_name="resource.calendar", string="Working Schedule", readonly=True)
    wage = fields.Monetary(string="Wage", readonly=True, help="Employee's monthly gross wage.")
    company_id = fields.Many2one(comodel_name="res.company", string="Company", readonly=True)
    company_country_id = fields.Many2one(comodel_name="res.country", string="Company country", readonly=True)
    country_code = fields.Char(string="Country Code", readonly=True, help="The ISO country code in two chars. \nYou can use this field for quick search.")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", readonly=True)
    contract_type_id = fields.Many2one(comodel_name="hr.contract.type", string="Contract Type", readonly=True)
    contract_ids = fields.One2many(comodel_name="hr.contract", inverse_name='parent_id', string="Contracts", readonly=True)
    contract_count = fields.Integer(string="# Contracts", readonly=True)
    under_contract_state = fields.Selection(selection=[["done","Under Contract"],["blocked","Not Under Contract"]], string="Contractual Status", readonly=True)
    activity_state = fields.Selection(selection=[["overdue","Overdue"],["today","Today"],["planned","Planned"]], string="Activity State", readonly=True, help="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
