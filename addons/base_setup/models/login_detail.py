# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LoginDetail(models.Model):
    _name = 'login.detail'
    _description = 'LOGIN DETAIL'
    _order = 'id desc'

    name = fields.Char(string="User Name")
    date_time = fields.Datetime(string="Login Date And Time")
    ip_address = fields.Char(string="IP Address")
