# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LinkTracker(models.Model):
    _name = 'link.tracker'
    _description = 'LINK TRACKER'
    _order = 'id desc'

    campaign_id = fields.Many2one(comodel_name="utm.campaign", string="Campaign", help="This is a name that helps you keep track of your different campaign efforts, e.g. Fall_Drive, Christmas_Special")
    source_id = fields.Many2one(comodel_name="utm.source", string="Source", help="This is the source of the link, e.g. Search Engine, another domain, or name of email list")
    medium_id = fields.Many2one(comodel_name="utm.medium", string="Medium", help="This is the method of delivery, e.g. Postcard, Email, or Banner Ad")
    url = fields.Char(string="Target URL", required=True)
    absolute_url = fields.Char(string="Absolute URL", readonly=True)
    short_url = fields.Char(string="Tracked URL", readonly=True)
    redirected_url = fields.Char(string="Redirected URL", readonly=True)
    short_url_host = fields.Char(string="Host of the short URL", readonly=True)
    title = fields.Char(string="Page Title")
    label = fields.Char(string="Button label")
    link_code_ids = fields.One2many(comodel_name="link.tracker.code", inverse_name='parent_id', string="Codes")
    code = fields.Char(string="Short URL code", readonly=True)
    link_click_ids = fields.One2many(comodel_name="link.tracker.click", inverse_name='parent_id', string="Clicks")
    count = fields.Integer(string="Number of Clicks", readonly=True)
    mass_mailing_id = fields.Many2one(comodel_name="mailing.mailing", string="Mass Mailing")
