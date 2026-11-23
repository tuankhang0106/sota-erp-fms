# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailChannel(models.Model):
    _name = 'mail.channel'
    _description = 'MAIL CHANNEL'
    _order = 'name'

    message_is_follower = fields.Boolean(string='Is Follower', readonly=True)
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='channel_id', string='Followers')
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='channel_id', string='Messages')
    has_message = fields.Boolean(string='Has Message', readonly=True)
    message_needaction = fields.Boolean(string='Action Needed', readonly=True, help='If checked, new messages require your attention.')
    message_needaction_counter = fields.Integer(string='Number of Actions', readonly=True, help='Number of messages requiring action')
    message_has_error = fields.Boolean(string='Message Delivery error', readonly=True, help='If checked, some messages have a delivery error.')
    message_has_error_counter = fields.Integer(string='Number of errors', readonly=True, help='Number of messages with delivery error')
    message_attachment_count = fields.Integer(string='Attachment Count', readonly=True)
    message_main_attachment_id = fields.Many2one(comodel_name='ir.attachment', string='Main Attachment')
    website_message_ids = fields.One2many(comodel_name='mail.message', inverse_name='channel_id', string='Website Messages', help='Website communication history')
    message_has_sms_error = fields.Boolean(string='SMS Delivery error', readonly=True, help='If checked, some messages have a delivery error.')
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', help='Set active to false to hide the channel without removing it.')
    channel_type = fields.Selection(selection=[["chat","Chat"],["channel","Channel"],["group","Group"]], string='Channel Type', required=True, readonly=True, help='Chat is private and unique between 2 persons. Group is private among invited persons. Channel can be freely joined (depending on its configuration).')
    is_chat = fields.Boolean(string='Is a chat', readonly=True)
    default_display_mode = fields.Selection(selection=[["video_full_screen","Full screen video"]], string='Default Display Mode', help='Determines how the channel will be displayed by default when opening it from its invitation link. No value means display text (no voice/video).')
    description = fields.Text(string='Description')
    image_128 = fields.Binary(string='Image')
    avatar_128 = fields.Binary(string='Avatar', readonly=True)
    channel_partner_ids = fields.Many2many(comodel_name='res.partner', string='Partners')
    channel_member_ids = fields.One2many(comodel_name='mail.channel.member', inverse_name='channel_id', string='Members')
    rtc_session_ids = fields.One2many(comodel_name='mail.channel.rtc.session', inverse_name='channel_id', string='Rtc Session')
    is_member = fields.Boolean(string='Is Member', readonly=True)
    member_count = fields.Integer(string='Member Count', readonly=True)
    group_ids = fields.Many2many(comodel_name='res.groups', string='Auto Subscription', help='Members of those groups will automatically added as followers. Note that they will be able to manage their subscription manually if necessary.')
    uuid = fields.Char(string='UUID')
    group_public_id = fields.Many2one(comodel_name='res.groups', string='Authorized Group')
    invitation_url = fields.Char(string='Invitation URL', readonly=True)
    subscription_department_ids = fields.Many2many(comodel_name='hr.department', string='HR Departments', help='Automatically subscribe members of those departments to the channel.')
