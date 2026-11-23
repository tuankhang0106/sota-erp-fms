# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MailThread(models.AbstractModel):
    _name = 'mail.thread'
    _description = 'Email Thread / Chatter Mixin'

    message_is_follower = fields.Boolean(string='Is Follower', compute='_compute_message_is_follower')
    message_follower_ids = fields.One2many(comodel_name='mail.followers', inverse_name='res_id', string='Followers')
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers (Partners)')
    message_ids = fields.One2many(comodel_name='mail.message', inverse_name='res_id', string='Messages', auto_join=True)
    message_unread = fields.Boolean(string='Unread Messages', compute='_compute_message_unread')
    message_unread_counter = fields.Integer(string='Unread Messages Counter', compute='_compute_message_unread')
    message_needaction = fields.Boolean(string='Action Needed', compute='_compute_message_needaction')
    message_needaction_counter = fields.Integer(string='Number of Actions', compute='_compute_message_needaction')
    message_has_error = fields.Boolean(string='Message Delivery error')
    message_has_error_counter = fields.Integer(string='Number of errors')
    message_attachment_count = fields.Integer(string='Attachment Count')

    def _compute_message_is_follower(self):
        for rec in self:
            rec.message_is_follower = False

    def _compute_message_unread(self):
        for rec in self:
            rec.message_unread = False
            rec.message_unread_counter = 0

    def _compute_message_needaction(self):
        for rec in self:
            rec.message_needaction = False
            rec.message_needaction_counter = 0

    def message_post(self, body='', subject=None, message_type='notification', subtype_xmlid=None, **kwargs):
        """ Post a new message on the thread """
        return self.env['mail.message'].create({
            'res_model': self._name,
            'res_id': self.id,
            'body': body,
            'subject': subject,
            'message_type': message_type,
            'author_id': self.env.user.partner_id.id,
        })
