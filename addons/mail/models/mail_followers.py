# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailFollowers(models.Model):
    _name = 'mail.followers'
    _description = 'MAIL FOLLOWERS'

    res_model = fields.Char(string='Related Document Model Name', required=True)
    res_id = fields.Char(string='Related Document ID')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Related Partner', required=True)
    subtype_ids = fields.Many2many(comodel_name='mail.message.subtype', string='Subtype', help='Message subtypes followed, meaning subtypes that will be pushed onto the user\'s Wall.')
    name = fields.Char(string='Name', readonly=True)
    email = fields.Char(string='Email', readonly=True)
    is_active = fields.Boolean(string='Is Active', readonly=True)
