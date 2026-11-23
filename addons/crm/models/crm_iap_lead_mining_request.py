# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmIapLeadMiningRequest(models.Model):
    _name = 'crm.iap.lead.mining.request'
    _description = 'CRM IAP LEAD MINING REQUEST'
    _order = 'id desc'

    name = fields.Char(string="Request Number", required=True, readonly=True)
    state = fields.Selection(selection=[["draft","Draft"],["error","Error"],["done","Done"]], string="Status", required=True)
    lead_number = fields.Integer(string="Number of Leads", required=True)
    search_type = fields.Selection(selection=[["companies","Companies"],["people","Companies and their Contacts"]], string="Target", required=True)
    error_type = fields.Selection(selection=[["credits","Insufficient Credits"],["no_result","No Result"]], string="Error Type", readonly=True)
    lead_type = fields.Selection(selection=[["lead","Leads"],["opportunity","Opportunities"]], string="Type", required=True)
    display_lead_label = fields.Char(string="Display Lead Label", readonly=True)
    team_id = fields.Many2one(comodel_name="crm.team", string="Sales Team")
    user_id = fields.Many2one(comodel_name="res.users", string="Salesperson")
    tag_ids = fields.Many2many(comodel_name="crm.tag", string="Tags")
    lead_ids = fields.One2many(comodel_name="crm.lead", inverse_name='parent_id', string="Generated Lead / Opportunity")
    lead_count = fields.Integer(string="Number of Generated Leads", readonly=True)
    filter_on_size = fields.Boolean(string="Filter on Size")
    company_size_min = fields.Integer(string="Size")
    company_size_max = fields.Integer(string="Company Size Max")
    country_ids = fields.Many2many(comodel_name="res.country", string="Countries")
    state_ids = fields.Many2many(comodel_name="res.country.state", string="States")
    available_state_ids = fields.One2many(comodel_name="res.country.state", inverse_name='parent_id', string="Available State", readonly=True)
    industry_ids = fields.Many2many(comodel_name="crm.iap.lead.industry", string="Industries")
    contact_number = fields.Integer(string="Number of Contacts")
    contact_filter_type = fields.Selection(selection=[["role","Role"],["seniority","Seniority"]], string="Filter on")
    preferred_role_id = fields.Many2one(comodel_name="crm.iap.lead.role", string="Preferred Role")
    role_ids = fields.Many2many(comodel_name="crm.iap.lead.role", string="Other Roles")
    seniority_id = fields.Many2one(comodel_name="crm.iap.lead.seniority", string="Seniority")
    lead_credits = fields.Char(string="Lead Credits", readonly=True)
    lead_contacts_credits = fields.Char(string="Lead Contacts Credits", readonly=True)
    lead_total_credits = fields.Char(string="Lead Total Credits", readonly=True)
