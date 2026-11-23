# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FreightOcrLog(models.Model):
    _name = 'freight.ocr.log'
    _description = 'FREIGHT OCR LOG'
    _order = 'id desc'

    user_id = fields.Many2one(comodel_name="res.users", string="User", readonly=True, help="Người bấm nút gọi API OCR.")
    ocr_type = fields.Selection(selection=[["sea_booking","SEA Booking Confirmation"],["air_booking","AIR Booking Confirmation"],["bill_of_lading","Bill of Lading"],["air_waybill","AIR Waybill"],["vendor_bill","Vendor Bill"],["other","Other"]], string="OCR API", readonly=True, help="Loại API OCR đã sử dụng (tương ứng nút bấm).")
    filename = fields.Char(string="File Name", readonly=True, help="Tên file đẩy vào OCR.")
    endpoint_url = fields.Char(string="Endpoint URL", readonly=True, help="URL API OCR đã gọi.")
    state = fields.Selection(selection=[["success","Success"],["error","Error"]], string="Status", readonly=True)
    response_text = fields.Text(string="Response", readonly=True, help="Response trả ra của API OCR (hoặc thông báo lỗi).")
    company_id = fields.Many2one(comodel_name="res.company", string="Company", readonly=True)
