# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountryWards(models.Model):
    _name = 'res.country.wards'
    _description = 'RES COUNTRY WARDS'
    _order = 'id desc'

    code = fields.Char(string="Wards Code")
    name = fields.Char(string="Wards Name")
    state_id = fields.Many2one(comodel_name="res.country.state", string="Province")
    active = fields.Boolean(string="Active")
    name_extension = fields.Char(string="Name Extension")
    is_vietnam_new_wards = fields.Boolean(string="Is Vietnam New Wards", help="Đánh dấu xã/phường thuộc danh sách 34 tỉnh thành mới theo Nghị quyết 202/2025/QH15")
