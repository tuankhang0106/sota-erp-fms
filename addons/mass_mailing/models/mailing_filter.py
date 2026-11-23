# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailingFilter(models.Model):
    _name = 'mailing.filter'
    _description = 'MAILING FILTER'
    _order = 'id desc'

    name = fields.Char(string="Filter Name", required=True)
    mailing_domain = fields.Char(string="Filter Domain", required=True)
    mailing_model_id = fields.Many2one(comodel_name="ir.model", string="Recipients Model", required=True)
    mailing_model_name = fields.Char(string="Recipients Model Name", readonly=True)
