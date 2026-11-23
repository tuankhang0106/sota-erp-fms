# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ShActivityAlarm(models.Model):
    _name = 'sh.activity.alarm'
    _description = 'SH ACTIVITY ALARM'

    name = fields.Char(string="Name", readonly=True)
    type = fields.Selection(selection=[["email","Email"],["popup","Popup"]], string="Type", required=True)
    sh_remind_before = fields.Integer(string="Reminder Before")
    sh_reminder_unit = fields.Selection(selection=[["Hour(s)","Hour(s)"],["Minute(s)","Minute(s)"],["Second(s)","Second(s)"]], string="Reminder Unit", required=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
