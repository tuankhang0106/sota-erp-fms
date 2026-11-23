# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountry(models.Model):
    _name = 'res.country'
    _description = 'RES COUNTRY'
    _order = 'id desc'

    name = fields.Char(string="Country Name", required=True)
    code = fields.Char(string="Country Code", help="The ISO country code in two chars. \nYou can use this field for quick search.")
    address_format = fields.Text(string="Layout in Reports", help="Display format to use for addresses belonging to this country.\n\nYou can use python-style string pattern with all the fields of the address (for example, use '%(street)s' to display the field 'street') plus\n%(state_name)s: the name of the state\n%(state_code)s: the code of the state\n%(country_name)s: the name of the country\n%(country_code)s: the code of the country")
    address_view_id = fields.Many2one(comodel_name="ir.ui.view", string="Input View", help="Use this field if you want to replace the usual way to encode a complete address. Note that the address_format field is used to modify the way to display addresses (in reports for example), while this field is used to modify the input form for addresses.")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    image_url = fields.Char(string="Flag", readonly=True, help="Url of static flag image")
    phone_code = fields.Integer(string="Country Calling Code")
    country_group_ids = fields.Many2many(comodel_name="res.country.group", string="Country Groups")
    state_ids = fields.One2many(comodel_name="res.country.state", inverse_name='parent_id', string="States")
    name_position = fields.Selection(selection=[["before","Before Address"],["after","After Address"]], string="Customer Name Position", help="Determines where the customer/company name should be placed, i.e. after or before the address.")
    vat_label = fields.Char(string="Vat Label", help="Use this field if you want to change vat label.")
    state_required = fields.Boolean(string="State Required")
    zip_required = fields.Boolean(string="Zip Required")
