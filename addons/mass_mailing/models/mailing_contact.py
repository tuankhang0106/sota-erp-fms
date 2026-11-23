# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailingContact(models.Model):
    _name = 'mailing.contact'
    _description = 'MAILING CONTACT'
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
    email_normalized = fields.Char(string="Normalized Email", readonly=True, help="This field is used to search on email address as the primary email field can contain more than strictly an email address.")
    is_blacklisted = fields.Boolean(string="Blacklist", readonly=True, help="If the email address is on the blacklist, the contact won't receive mass mailing anymore, from any list")
    message_bounce = fields.Integer(string="Bounce", help="Counter of the number of bounced emails for this contact")
    name = fields.Char(string="Name")
    company_name = fields.Char(string="Company Name")
    title_id = fields.Many2one(comodel_name="res.partner.title", string="Title")
    email = fields.Char(string="Email")
    list_ids = fields.Many2many(comodel_name="mailing.list", string="Mailing Lists")
    subscription_list_ids = fields.One2many(comodel_name="mailing.contact.subscription", inverse_name='parent_id', string="Subscription Information")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")
    tag_ids = fields.Many2many(comodel_name="res.partner.category", string="Tags")
    opt_out = fields.Boolean(string="Opt Out", readonly=True, help="Opt out flag for a specific mailing list. This field should not be used in a view without a unique and active mailing list context.")
