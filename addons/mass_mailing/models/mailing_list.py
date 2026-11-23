# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailingList(models.Model):
    _name = 'mailing.list'
    _description = 'MAILING LIST'
    _order = 'id desc'

    name = fields.Char(string="Mailing List", required=True)
    active = fields.Boolean(string="Active")
    contact_count = fields.Integer(string="Number of Contacts", readonly=True)
    contact_count_email = fields.Integer(string="Number of Emails", readonly=True)
    contact_count_opt_out = fields.Integer(string="Number of Opted-out", readonly=True)
    contact_pct_opt_out = fields.Float(string="Percentage of Opted-out", readonly=True)
    contact_count_blacklisted = fields.Integer(string="Number of Blacklisted", readonly=True)
    contact_pct_blacklisted = fields.Float(string="Percentage of Blacklisted", readonly=True)
    contact_pct_bounce = fields.Float(string="Percentage of Bouncing", readonly=True)
    contact_ids = fields.Many2many(comodel_name="mailing.contact", string="Mailing Lists")
    mailing_count = fields.Integer(string="Number of Mailing", readonly=True)
    mailing_ids = fields.Many2many(comodel_name="mailing.mailing", string="Mass Mailings")
    subscription_ids = fields.One2many(comodel_name="mailing.contact.subscription", inverse_name='parent_id', string="Subscription Information")
    is_public = fields.Boolean(string="Show In Preferences", help="The mailing list can be accessible by recipients in the subscription management page to allows them to update their preferences.")
