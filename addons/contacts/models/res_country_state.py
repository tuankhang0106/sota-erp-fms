# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountryState(models.Model):
    _name = 'res.country.state'
    _description = 'RES COUNTRY STATE'
    _order = 'id desc'

    country_id = fields.Many2one(comodel_name="res.country", string="Country", required=True)
    name = fields.Char(string="State Name", required=True, help="Administrative divisions of a country. E.g. Fed. State, Departement, Canton")
    code = fields.Char(string="State Code", required=True, help="The state code.")
    accents = fields.Char(string="Accents")
    active = fields.Boolean(string="Active")
    wards_ids = fields.One2many(comodel_name="res.country.wards", inverse_name='parent_id', string="Ward")
    name_extension = fields.Char(string="Name Extension")
    is_vietnam_new_province = fields.Boolean(string="Is Vietnam New Province", help="Đánh dấu tỉnh thành thuộc danh sách 34 tỉnh thành mới theo Nghị quyết 202/2025/QH15")
    old_province_mapping = fields.Text(string="Old Province Mapping", help="Danh sách các tỉnh thành cũ được sáp nhập vào tỉnh thành này (JSON format)")
    sequence_id = fields.Many2one(comodel_name="ir.sequence", string="Sequence")
