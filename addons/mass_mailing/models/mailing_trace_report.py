# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailingTraceReport(models.Model):
    _name = 'mailing.trace.report'
    _description = 'MAILING TRACE REPORT'
    _order = 'id desc'

    name = fields.Char(string="Mass Mail", readonly=True)
    mailing_type = fields.Selection(selection=[["mail","Mail"]], string="Type", required=True)
    campaign = fields.Char(string="Mailing Campaign", readonly=True)
    scheduled_date = fields.Datetime(string="Scheduled Date", readonly=True)
    state = fields.Selection(selection=[["draft","Draft"],["test","Tested"],["done","Sent"]], string="Status", readonly=True)
    email_from = fields.Char(string="From", readonly=True)
    scheduled = fields.Integer(string="Scheduled", readonly=True)
    sent = fields.Integer(string="Sent", readonly=True)
    delivered = fields.Integer(string="Delivered", readonly=True)
    error = fields.Integer(string="Error", readonly=True)
    opened = fields.Integer(string="Opened", readonly=True)
    replied = fields.Integer(string="Replied", readonly=True)
    bounced = fields.Integer(string="Bounced", readonly=True)
    canceled = fields.Integer(string="Canceled", readonly=True)
    clicked = fields.Integer(string="Clicked", readonly=True)
