# -*- coding: utf-8 -*-
from odoo import models, fields, api

class GdtEinvoiceBill(models.Model):
    _name = 'gdt.einvoice.bill'
    _description = 'GDT EINVOICE BILL'
    _order = 'id desc'

    seller_tax_code = fields.Char(string="MST người bán")
    seller_name = fields.Char(string="Tên người bán")
    seller_address = fields.Char(string="Địa chỉ người bán")
    buyer_tax_code = fields.Char(string="MST người mua")
    buyer_name = fields.Char(string="Tên người mua")
    buyer_address = fields.Char(string="Địa chỉ người mua")
    invoice_type_name = fields.Char(string="Loại hóa đơn")
    invoice_template = fields.Char(string="Mẫu số")
    invoice_symbol = fields.Char(string="Ký hiệu")
    invoice_number = fields.Char(string="Số hóa đơn")
    tax_authority_code = fields.Char(string="Mã cơ quan thuế")
    invoice_date = fields.Date(string="Ngày lập")
    signing_date = fields.Datetime(string="Ngày ký")
    currency_code = fields.Char(string="Loại tiền")
    exchange_rate = fields.Float(string="Tỷ giá")
    total_before_tax = fields.Float(string="Tiền trước thuế")
    tax_amount = fields.Float(string="Tiền thuế")
    total_amount = fields.Float(string="Tổng tiền thanh toán")
    total_amount_text = fields.Char(string="Số tiền bằng chữ")
    tax_rate_info = fields.Char(string="Thuế suất", help="Thông tin thuế suất từ GDT")
    payment_method = fields.Char(string="Hình thức thanh toán")
    invoice_status = fields.Selection(selection=[["1","Hóa đơn mới"],["2","Hóa đơn thay thế"],["3","Hóa đơn điều chỉnh"],["4","Hóa đơn đã bị thay thế"],["5","Hóa đơn đã bị điều chỉnh"],["6","Hóa đơn đã hủy"]], string="Trạng thái HĐ")
    processing_status = fields.Selection(selection=[["0","Chưa xử lý"],["1","Đang xử lý"],["5","Đã cấp mã"],["6","CQT không cấp mã"],["8","HĐ có mã khởi tạo từ MTT"]], string="Trạng thái xử lý")
    check_result = fields.Char(string="Kết quả kiểm tra")
    is_risk = fields.Boolean(string="Rủi ro", help="Vendor sử dụng hóa đơn bất hợp pháp theo danh sách của GDT")
    gdt_invoice_id = fields.Char(string="GDT Invoice ID", readonly=True)
    note = fields.Text(string="Ghi chú")
    raw_data = fields.Text(string="Dữ liệu gốc (JSON)")
    company_id = fields.Many2one(comodel_name="res.company", string="Công ty", required=True)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Loại tiền tệ")
    vendor_bill_id = fields.Many2one(comodel_name="account.move", string="Tham chiếu hóa đơn")
    bill_check = fields.Selection(selection=[["same","Khớp tiền"],["warning","Lệch tiền"],["no_data","Chưa có vendor bill"]], string="Khớp tiền", readonly=True)
    vendor_bill_count = fields.Integer(string="Vendor Bill", readonly=True)
