# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sh_display_multi_user = fields.Boolean(string='Enable Multi User Activity Assignment')
    sh_activity_alarm = fields.Boolean(string='Enable Activity Alarms')
