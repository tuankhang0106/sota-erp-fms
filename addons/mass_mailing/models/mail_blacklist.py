# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailBlacklist(models.Model):
    _name = 'mail.blacklist'
    _description = 'MAIL BLACKLIST'
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
    email = fields.Char(string="Email Address", required=True, help="This field is case insensitive.")
    active = fields.Boolean(string="Active")
