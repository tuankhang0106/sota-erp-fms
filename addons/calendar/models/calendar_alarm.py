# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CalendarAlarm(models.Model):
    _name = 'calendar.alarm'
    _description = 'CALENDAR ALARM'

    name = fields.Char(string="Name", required=True)
    alarm_type = fields.Selection(selection=[["notification","Notification"],["email","Email"],["sms","SMS Text Message"]], string="Type", required=True)
    duration = fields.Integer(string="Remind Before", required=True)
    interval = fields.Selection(selection=[["minutes","Minutes"],["hours","Hours"],["days","Days"]], string="Unit", required=True)
    duration_minutes = fields.Integer(string="Duration in minutes", readonly=True)
    mail_template_id = fields.Many2one(comodel_name="mail.template", string="Email Template", help="Template used to render mail reminder content.")
    body = fields.Text(string="Additional Message", help="Additional message that would be sent with the notification for the reminder")
    sms_template_id = fields.Many2one(comodel_name="sms.template", string="SMS Template", help="Template used to render SMS reminder content.")
