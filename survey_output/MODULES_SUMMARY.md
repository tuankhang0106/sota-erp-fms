# DANH SÁCH TOÀN BỘ CÁC MODULE VÀ MENU TRONG HỆ THỐNG SOTA ERP

**Thời gian khảo sát:** 2026-11-21T08:29:53.023Z
**URL:** https://portalink.erp.sota-solutions.com/
**Tổng số Module gốc (Apps):** 15

## 📦 Module: Thảo luận
- **ID:** 74 | **Action:** 107 | **XML ID:** `mail.menu_root_discuss`
*(Module đơn cấp, không có sub-menu)*

---

## 📦 Module: Lịch
- **ID:** 117 | **Action:** 181 | **XML ID:** `calendar.mail_menu_calendar`
*(Module đơn cấp, không có sub-menu)*

---

## 📦 Module: Activity Dashboard
- **ID:** 164 | **Action:** 257 | **XML ID:** `sh_activities_management.sh_activity_dashboard`

### Các Menu con (Submenus / Features):
- **Dashboard** (ID: 175, Action: 257, XML: `sh_activities_management.sh_menu_activity_dashboard`)
- **Activity** (ID: 169, Action: 251, XML: `sh_activities_management.sh_activity`)
  - **All Activities** (ID: 170, Action: 251, XML: `sh_activities_management.all_activity`)
  - **Supervisor Activities** (ID: 171, Action: 254, XML: `sh_activities_management.sh_supervisor_activity`)
  - **My Activities** (ID: 172, Action: 253, XML: `sh_activities_management.sh_my_activity`)
- **Reporting** (ID: 174, Action: 252, XML: `sh_activities_management.reporting`)
- **Configuration** (ID: 165, XML: `sh_activities_management.menu_config`)
  - **Activity Tags** (ID: 173, Action: 255, XML: `sh_activities_management.sh_activity_tags`)
  - **Activity Alarm** (ID: 166, Action: 245, XML: `sh_activities_management.sh_activity_alarm_manu`)
  - **Settings** (ID: 167, Action: 233, XML: `sh_activities_management.menu_config_activity`)

---

## 📦 Module: Vận chuyển
- **ID:** 309 | **Action:** 638 | **XML ID:** `sota_freight_crm.menu_freight`

### Các Menu con (Submenus / Features):
- **Báo giá** (ID: 331, XML: `sota_freight_crm.freight_quotation_menu_parent`)
  - **Báo giá** (ID: 332, Action: 454, XML: `sota_freight_crm.freight_quotation_menu`)
- **Dashboard FMS** (ID: 587, Action: 859)
- **Quản lý Job** (ID: 437, XML: `sota_freight_advanced.menu_freight_job_management`)
  - **Quản lý Job** (ID: 509, XML: `sota_freight_advanced.freight_job_menu1`)
    - **Job** (ID: 510, Action: 638, XML: `sota_freight_advanced.freight_job_menu2`)
  - **Quản lý House** (ID: 438, XML: `sota_freight_advanced.menu_freight_house_management`)
    - **House Sea B/L** (ID: 443, Action: 624, XML: `sota_freight_advanced.freight_shipment_house_menu`)
    - **House Air B/L** (ID: 444, Action: 625, XML: `sota_freight_advanced.freight_shipment_house_air`)
    - **House Cross Border** (ID: 534, Action: 761, XML: `sota_freight_advanced_v2.freight_shipment_house_multi_menu`)
  - **Quản lý Master** (ID: 439, XML: `sota_freight_advanced.menu_freight_master_management`)
    - **Master SEA B/L** (ID: 445, Action: 626, XML: `sota_freight_advanced.freight_shipment_sea_master_menu`)
    - **Master AIR B/L** (ID: 446, Action: 627, XML: `sota_freight_advanced.freight_shipment_air_master_menu`)
    - **Master Cross Border** (ID: 535, Action: 762, XML: `sota_freight_advanced_v2.freight_shipment_master_multi_menu`)
- **Quản lý thanh toán** (ID: 454, Action: 634, XML: `sota_freight_advanced.freight_credit_note_menu`)
  - **Credit Note** (ID: 530, Action: 634, XML: `sota_freight_advanced.freight_credit_note_submenu`)
  - **Bảng tổng hợp công nợ** (ID: 531, Action: 749, XML: `sota_freight_advanced.menu_freight_soa_credit`)
- **Debit Note / SOA** (ID: 515, XML: `sota_freight_advanced.freight_debit_note_menu_parent`)
  - **Debit Note** (ID: 455, Action: 635, XML: `sota_freight_advanced.freight_debit_note_menu`)
  - **Bảng tổng hợp công nợ** (ID: 517, Action: 719, XML: `sota_freight_advanced.menu_freight_soa_debit`)
- **DC Note / SOA** (ID: 514, XML: `sota_freight_advanced.freight_dc_note_menu_parent`)
  - **DC Note** (ID: 467, Action: 648, XML: `sota_freight_advanced.freight_dc_note_menu`)
  - **Bảng tổng hợp công nợ** (ID: 516, Action: 718, XML: `sota_freight_advanced.menu_freight_soa_dc`)
  - **SOA Debt Offset** (ID: 596, Action: 875, XML: `sota_freight_advanced.menu_freight_soa_debt_offset`)
- **Giá cả** (ID: 526, XML: `sota_freight_crm.menu_freight_pricing`)
  - **Bảng giá mua** (ID: 527, Action: 746, XML: `sota_freight_crm.menu_freight_purchase_pricing`)
  - **Yêu cầu báo giá** (ID: 529, Action: 748, XML: `sota_freight_crm.freight_sales_inquiry_menu`)
- **Liên hệ** (ID: 554, XML: `sota_freight_crm.menu_freight_contact`)
  - **Đối tác** (ID: 556, Action: 436, XML: `sota_freight_crm.menu_freight_partner`)
  - **Người phụ trách** (ID: 555, Action: 435, XML: `sota_freight_crm.menu_freight_pics`)
- **Báo cáo** (ID: 441, XML: `sota_freight_advanced.menu_freight_report`)
  - **Báo cáo hiệu suất** (ID: 468, Action: 672, XML: `sota_freight_advanced.freight_performance_report_menu`)
  - **Lợi nhuận Job theo ngày thực hiện** (ID: 469, Action: 673, XML: `sota_freight_advanced.freight_selling_profit_by_job_perf_date_menu`)
  - **Báo cáo quản trị theo lô hàng** (ID: 602, Action: 880, XML: `sota_freight_advanced_v2.menu_freight_daily_performance`)
  - **Lợi nhuận Job theo ngày TH (mới)** (ID: 594, Action: 868, XML: `sota_freight_advanced_v2.menu_job_profit_perf_date_new`)
  - **Báo cáo chi tiết doanh thu giá vốn** (ID: 613, Action: 902, XML: `sota_freight_advanced_v2.menu_freight_dp_detail`)
  - **Phân tích P/L theo ngày thực hiện** (ID: 545, XML: `sota_freight_advanced_v2.menu_freight_pl_detail_reports`)
    - **P/L theo phòng ban** (ID: 546, Action: 763, XML: `sota_freight_advanced_v2.menu_freight_pl_by_ops`)
    - **P/L theo nhân viên KD** (ID: 547, Action: 764, XML: `sota_freight_advanced_v2.menu_freight_pl_by_salesman`)
    - **P/L Snapshots** (ID: 579, Action: 840, XML: `sota_freight_advanced_v2.menu_freight_pl_snapshot`)
- **Cấu hình** (ID: 310, XML: `sota_freight_crm.menu_freight_configuration`)
  - **Cài đặt** (ID: 335, Action: 456, XML: `sota_freight_crm.view_freight_setting_menu`)
  - **Nhà vận chuyển** (ID: 311, XML: `sota_freight_crm.menu_freight_transportation_carrier`)
    - **Hãng hàng không** (ID: 315, Action: 437, XML: `sota_freight_crm.menu_airline`)
    - **Hãng vận tải biển** (ID: 316, Action: 438, XML: `sota_freight_crm.menu_freight_shipping_line`)
    - **Hãng xe** (ID: 325, Action: 447, XML: `sota_freight_crm.menu_trucker`)
  - **Sản phẩm** (ID: 313, XML: `sota_freight_crm.menu_freight_product`)
    - **Dịch vụ Vận tải** (ID: 314, Action: 433, XML: `sota_freight_crm.menu_freight_product_service`)
    - **Local Charge Vendor** (ID: 597, Action: 876, XML: `sota_freight_crm.menu_freight_local_charge`)
    - **Local Charge Carrier** (ID: 598, Action: 877, XML: `sota_freight_crm.menu_freight_local_charge_carrier`)
  - **Cargo & Products** (ID: 589, XML: `sota_freight_crm.menu_freight_cargo_products`)
    - **Container/Đơn vị** (ID: 326, Action: 448, XML: `sota_freight_crm.menu_freight_unit`)
    - **Đơn vị FCL** (ID: 525, Action: 743, XML: `sota_freight_crm.menu_freight_fcl_unit`)
    - **Kiện hàng** (ID: 320, Action: 442, XML: `sota_freight_crm.menu_package`)
    - **Hàng hóa** (ID: 317, Action: 439, XML: `sota_freight_crm.menu_freight_commodity`)
  - **Locations & Routes** (ID: 590, XML: `sota_freight_crm.menu_freight_locations`)
    - **Cảng** (ID: 322, Action: 444, XML: `sota_freight_crm.menu_port`)
    - **Tàu** (ID: 327, Action: 449, XML: `sota_freight_crm.menu_freight_vesel`)
    - **Loại hình vận chuyển** (ID: 324, Action: 446, XML: `sota_freight_crm.menu_freight_transit_type`)
  - **Customs** (ID: 591, XML: `sota_freight_crm.menu_freight_customs`)
    - **Mã HS** (ID: 318, Action: 440, XML: `sota_freight_crm.menu_freight_hs_code`)
    - **Mã thủ tục** (ID: 466, Action: 647, XML: `sota_freight_advanced.menu_procedure_code_information`)
    - **Số quản lý** (ID: 459, Action: 639, XML: `sota_freight_advanced.menu_freight_bl_number`)
  - **Commercial Terms** (ID: 592, XML: `sota_freight_crm.menu_freight_commercial_terms`)
    - **Incoterms** (ID: 319, Action: 441, XML: `sota_freight_crm.menu_freight_incoterms`)
    - **Điều khoản dịch vụ** (ID: 323, Action: 445, XML: `sota_freight_crm.menu_freight_service_terms`)
    - **Vai trò đối tác** (ID: 321, Action: 443, XML: `sota_freight_crm.menu_freight_party_role`)
    - **Nhãn dịch vụ** (ID: 448, Action: 629, XML: `sota_freight_advanced.menu_freight_service_tags`)
  - **Finance** (ID: 593, XML: `sota_freight_crm.menu_freight_finance`)
    - **Bank Information** (ID: 465, Action: 646, XML: `sota_freight_advanced.menu_bank_information`)
    - **Tài khoản nhà cung cấp** (ID: 461, Action: 641, XML: `sota_freight_advanced.vendor_menu`)
    - **Banks** (ID: 599, Action: 61, XML: `sota_freight_crm.menu_freight_res_bank`)
    - **Tiền tệ** (ID: 312, Action: 67, XML: `sota_freight_crm.menu_freight_curency_rate`)
    - **Hợp đồng nhà cung cấp** (ID: 462, Action: 642, XML: `sota_freight_advanced.menu_freight_vendor_contract`)
    - **Transfer Cost Config** (ID: 575, Action: 829, XML: `sota_freight_advanced_v2.menu_freight_transfer_cost_config`)
    - **Quantity Rules** (ID: 573, Action: 824, XML: `sota_freight_advanced.menu_freight_qty_rule_global`)
  - **Hồ sơ quyền báo cáo quản trị** (ID: 603, Action: 881, XML: `sota_freight_advanced_v2.menu_freight_dp_access_profile`)
  - **Mã DT / Mã GV** (ID: 614, Action: 903, XML: `sota_freight_advanced_v2.menu_freight_dp_account_code`)
  - **Trình gộp nhân viên KD** (ID: 471, Action: 676, XML: `sota_freight_advanced.wizard_merge_salesman_menu`)
  - **Địa chỉ D/O** (ID: 552, Action: 772, XML: `sota_freight_advanced_v2.menu_do_address`)

---

## 📦 Module: My Dashboard
- **ID:** 582 | **Action:** 843 | **XML ID:** `ks_dashboard_ninja.board_menu_root`

### Các Menu con (Submenus / Features):
- **Configuration** (ID: 583, XML: `ks_dashboard_ninja.configuration_menu`)
  - **Dashboards** (ID: 584, Action: 844, XML: `ks_dashboard_ninja.dashboard_menu`)
  - **Dashboard Layouts** (ID: 585, Action: 846, XML: `ks_dashboard_ninja.dashboard_layout_menu`)
  - **Import Dashboards** (ID: 586, Action: 852, XML: `ks_dashboard_ninja.ks_import_dashboard_menu`)

---

## 📦 Module: Mass Activities Dynamic Action
- **ID:** 168 | **Action:** 250 | **XML ID:** `sh_activities_management.sh_activity_management_dynamic_action_action_menu`
*(Module đơn cấp, không có sub-menu)*

---

## 📦 Module: Liên hệ
- **ID:** 123 | **Action:** 436 | **XML ID:** `contacts.menu_contacts`

### Các Menu con (Submenus / Features):
- **Liên hệ** (ID: 124, Action: 436, XML: `contacts.res_partner_menu_contacts`)
- **Người phụ trách** (ID: 612, Action: 435, XML: `sota_freight_crm.menu_contacts_freight_pics`)
- **Cấu hình** (ID: 125, XML: `contacts.res_partner_menu_config`)
  - **Thẻ liên hệ** (ID: 126, Action: 59, XML: `contacts.menu_partner_category_form`)
  - **Danh xưng** (ID: 127, Action: 55, XML: `contacts.menu_partner_title_contact`)
  - **Ngành nghề ** (ID: 128, Action: 60, XML: `contacts.res_partner_industry_menu`)
  - **Bản địa hóa** (ID: 129, XML: `contacts.menu_localisation`)
    - **Quốc gia** (ID: 130, Action: 63, XML: `contacts.menu_country_partner`)
    - **Tỉnh/TP/Bang** (ID: 132, Action: 65, XML: `contacts.menu_country_state_partner`)
    - **Nhóm quốc gia** (ID: 131, Action: 64, XML: `contacts.menu_country_group`)
    - **Phường/Xã/Thị trấn** (ID: 345, Action: 485, XML: `sota_vn_address.menu_action_wards`)
  - **Tài khoản ngân hàng** (ID: 133, XML: `contacts.menu_config_bank_accounts`)
    - **Ngân hàng** (ID: 134, Action: 61, XML: `contacts.menu_action_res_bank_form`)
    - **Tài khoản ngân hàng** (ID: 135, Action: 62, XML: `contacts.menu_action_res_partner_bank_form`)

---

## 📦 Module: CRM
- **ID:** 231 | **Action:** 450 | **XML ID:** `crm.crm_menu_root`

### Các Menu con (Submenus / Features):
- **Bán hàng** (ID: 232, XML: `crm.crm_menu_sales`)
  - **Khách hàng** (ID: 236, Action: 450, XML: `crm.res_partner_menu_customer`)
  - **Lead** (ID: 328, Action: 451, XML: `crm.res_partner_menu_customer_lead`)
  - **Hoạt động của tôi** (ID: 234, Action: 356, XML: `crm.crm_lead_menu_my_activities`)
  - **Báo giá** (ID: 333, Action: 454, XML: `sota_freight_crm.freight_quotation_crm_menu`)
  - **Đội ngũ** (ID: 235, Action: 229, XML: `crm.sales_team_menu_team_pipeline`)
  - **Người phụ trách** (ID: 329, Action: 452, XML: `sota_freight_crm.res_partner_menu_pic`)
- **Cước** (ID: 536, XML: `sota_freight_advanced_v2.menu_freight_crm`)
  - **Quản lý Job** (ID: 537, Action: 638, XML: `sota_freight_advanced_v2.menu_freight_job_management_crm`)
  - **Quản lý House** (ID: 538, XML: `sota_freight_advanced_v2.menu_freight_house_management_crm`)
    - **House Sea B/L** (ID: 539, Action: 624, XML: `sota_freight_advanced_v2.freight_shipment_house_sea_crm`)
    - **House Air B/L** (ID: 540, Action: 625, XML: `sota_freight_advanced_v2.freight_shipment_house_air_crm`)
  - **Bảng giá** (ID: 541, XML: `sota_freight_advanced_v2.menu_freight_pricing_crm`)
    - **Bảng giá mua** (ID: 542, Action: 746, XML: `sota_freight_advanced_v2.menu_freight_purchase_pricing_crm`)
    - **Yêu cầu báo giá** (ID: 543, Action: 748, XML: `sota_freight_advanced_v2.freight_sales_inquiry_menu_crm`)
- **Các kỳ KPI** (ID: 330, Action: 453, XML: `sota_freight_crm.menu_crm_kpi_period`)
- **Dashboard CRM** (ID: 588, Action: 860)
- **Báo cáo** (ID: 238, XML: `crm.crm_menu_report`)
  - **Báo cáo kinh doanh** (ID: 601, Action: 879, XML: `sota_freight_crm.menu_crm_sales_report`)
  - **KPI** (ID: 336, Action: 457, XML: `sota_freight_crm.crm_kpi_report_menu`)
- **Cấu hình** (ID: 243, Action: 341, XML: `crm.crm_menu_config`)
  - **Cài đặt** (ID: 244, Action: 361, XML: `crm.crm_config_settings_menu`)
  - **Đội ngũ kinh doanh bán hàng** (ID: 246, Action: 230, XML: `crm.crm_team_config`)
  - **Phòng kinh doanh** (ID: 334, Action: 455, XML: `sota_freight_crm.sales_department_config_menu`)
  - **Nguồn khách hàng** (ID: 600, Action: 878, XML: `sota_freight_crm.res_partner_resource_config_menu`)
  - **Loại hoạt động** (ID: 248, Action: 232, XML: `crm.crm_team_menu_config_activity_types`)
  - **Kế hoạch định kỳ** (ID: 249, Action: 349, XML: `crm.crm_recurring_plan_menu_config`)
  - **Quy trình** (ID: 250, XML: `crm.menu_crm_config_lead`)
    - **Thẻ** (ID: 252, Action: 59, XML: `crm.menu_crm_lead_categ`)
    - **Lý do mất** (ID: 253, Action: 350, XML: `crm.menu_crm_lost_reason`)
  - **Tạo lead** (ID: 340, XML: `crm_iap_mine.crm_menu_lead_generation`)
    - **Yêu cầu tìm lead** (ID: 341, Action: 472, XML: `crm_iap_mine.crm_iap_lead_mining_request_menu_action`)

---

## 📦 Module: Bảng điều khiển
- **ID:** 158 | **Action:** 234 | **XML ID:** `spreadsheet_dashboard.spreadsheet_dashboard_menu_root`

### Các Menu con (Submenus / Features):
- **Bảng điều khiển** (ID: 159, Action: 234, XML: `spreadsheet_dashboard.spreadsheet_dashboard_menu_dashboard`)
- **Cấu hình** (ID: 160, XML: `spreadsheet_dashboard.spreadsheet_dashboard_menu_configuration`)
  - **Bảng điều khiển** (ID: 161, Action: 235, XML: `spreadsheet_dashboard.spreadsheet_dashboard_menu_configuration_dashboards`)

---

## 📦 Module: Kế toán
- **ID:** 178 | **Action:** 333 | **XML ID:** `account.menu_finance`

### Các Menu con (Submenus / Features):
- **Bảng thông tin** (ID: 179, Action: 333, XML: `account.menu_board_journal_1`)
- **Khách hàng** (ID: 180, XML: `account.menu_finance_receivables`)
  - **Hóa đơn** (ID: 181, Action: 300, XML: `account.menu_action_move_out_invoice_type`)
  - **Hóa đơn điều chỉnh** (ID: 182, Action: 301, XML: `account.menu_action_move_out_refund_type`)
  - **Nhận hàng** (ID: 183, Action: 304, XML: `account.menu_action_move_out_receipt_type`)
  - **Giấy báo có** (ID: 548, Action: 768, XML: `sota_freight_advanced_v2.menu_action_account_payments_receivable_bank`)
  - **Phiếu thu** (ID: 549, Action: 769, XML: `sota_freight_advanced_v2.menu_action_account_payments_receivable_cash`)
  - **Luân chuyển nội bộ (Mua bán ngoại tệ)** (ID: 576, Action: 834, XML: `sota_freight_advanced_v2.menu_action_account_payments_internal_transfer_receivable`)
  - **Sản phẩm** (ID: 185, Action: 322, XML: `account.product_product_menu_sellable`)
  - **Khách hàng** (ID: 186, Action: 331, XML: `account.menu_account_customer`)
- **Nhà cung cấp** (ID: 187, XML: `account.menu_finance_payables`)
  - **Hoá đơn** (ID: 188, Action: 302, XML: `account.menu_action_move_in_invoice_type`)
  - **Hoàn tiền** (ID: 189, Action: 303, XML: `account.menu_action_move_in_refund_type`)
  - **Nhận hàng** (ID: 190, Action: 305, XML: `account.menu_action_move_in_receipt_type`)
  - **Giấy báo nợ** (ID: 550, Action: 770, XML: `sota_freight_advanced_v2.menu_action_account_payments_payable_bank`)
  - **Phiếu chi** (ID: 551, Action: 771, XML: `sota_freight_advanced_v2.menu_action_account_payments_payable_cash`)
  - **Chi phí nhân viên** (ID: 306, Action: 425, XML: `hr_expense.menu_hr_expense_account_employee_expenses`)
  - **Luân chuyển nội bộ (Mua bán ngoại tệ)** (ID: 577, Action: 834, XML: `sota_freight_advanced_v2.menu_action_account_payments_internal_transfer_payable`)
  - **Hóa đơn đầu vào (GDT)** (ID: 567, Action: 800, XML: `sota_sync_einvoice_bill.menu_gdt_einvoice_bill`)
  - **Sản phẩm** (ID: 192, Action: 323, XML: `account.product_product_menu_purchasable`)
  - **Nhà cung cấp** (ID: 193, Action: 332, XML: `account.menu_account_supplier`)
- **Kế toán** (ID: 194, XML: `account.menu_finance_entries`)
  - **Các sổ nhật ký** (ID: 195, XML: `account.menu_finance_entries_accounting_miscellaneous`)
    - **Bút toán phát sinh** (ID: 196, Action: 299, XML: `account.menu_action_move_journal_line_form`)
    - **Chi tiết bút toán** (ID: 197, Action: 298, XML: `account.menu_action_account_moves_all`)
  - **Quản lý** (ID: 198, XML: `account.menu_finance_entries_management`)
    - **Kết chuyển số dư tài khoản** (ID: 571, Action: 807, XML: `sota_account_closing_entry_forward.account_balance_carry_forward_menu`)
    - **Bút toán phát sinh quản trị** (ID: 199, Action: 173, XML: `account.menu_action_analytic_lines_tree`)
    - **Tài sản** (ID: 559, Action: 781, XML: `sota_account_asset.menu_action_account_asset_asset`)
  - **Tác vụ** (ID: 201, XML: `account.menu_finance_entries_actions`)
    - **Reconcile** (ID: 572, Action: 814, XML: `account_reconcile_oca.account_account_reconcile_menu`)
    - **Lock Dates** (ID: 532, Action: 751, XML: `om_fiscal_year.menu_action_change_lock_date`)
  - **Transfer Service Cost** (ID: 574, Action: 828, XML: `sota_freight_advanced_v2.menu_freight_transfer_service_cost`)
- **Báo cáo** (ID: 202, XML: `account.menu_finance_reports`)
  - **Báo cáo sao kê** (ID: 205, XML: `account.account_reports_legal_statements_menu`)
    - **Bảng cân đối kế toán** (ID: 349, Action: 487, XML: `to_account_reports.balance_sheet_client_menu`)
    - **Lãi và lỗ** (ID: 350, Action: 488, XML: `to_account_reports.profit_and_loss_client_menu`)
    - **Báo cáo lưu chuyển tiền tệ** (ID: 351, Action: 489, XML: `to_account_reports.cash_flow_client_menu`)
    - **Bảng tóm tắt Hoạt động** (ID: 352, Action: 490, XML: `to_account_reports.executive_summary_client_menu`)
    - **Báo cáo thuế** (ID: 353, Action: 491, XML: `to_account_reports.tax_report_client_menu`)
  - **Báo cáo kiểm toán** (ID: 346, XML: `to_account_reports.audit_reports_root_menu`)
    - **Sổ cái** (ID: 354, Action: 492, XML: `to_account_reports.general_ledger_client_menu`)
    - **Bảng cân đối phát sinh** (ID: 355, Action: 493, XML: `to_account_reports.trial_balance_client_menu`)
  - **Báo cáo kế toán Việt Nam** (ID: 344, XML: `l10n_vn_viin.account_reports_vn_menu`)
    - **Sổ chi tiết tài khoản (S38-DN)** (ID: 360, Action: 502, XML: `l10n_vn_viin_account_reports.l10n_vn_s38dn_menu`)
    - **Sổ nhật ký chung (S03a-DN)** (ID: 361, Action: 503, XML: `l10n_vn_viin_account_reports.l10n_vn_s03adn_menu`)
    - **Sổ cái (S03b-DN)** (ID: 362, Action: 504, XML: `l10n_vn_viin_account_reports.l10n_vn_s03bdn_menu`)
    - **Sổ quỹ tiền mặt (S07-DN)** (ID: 363, Action: 505, XML: `l10n_vn_viin_account_reports.l10n_vn_s07dn_menu`)
    - **Sổ tiền gửi ngân hàng (S08-DN)** (ID: 364, Action: 506, XML: `l10n_vn_viin_account_reports.l10n_vn_s08dn_menu`)
  - **Báo cáo đối tác** (ID: 347, XML: `to_account_reports.partner_reports_root_menu`)
    - **Sổ cái đối tác** (ID: 356, Action: 494, XML: `to_account_reports.partner_ledger_client_menu`)
    - **Chi tiết công nợ phải thu theo hóa đơn** (ID: 610, Action: 887, XML: `sota_freight_advanced_v2.menu_freight_ar_invoice_detail`)
    - **Phân tích công nợ phải thu** (ID: 611, Action: 888, XML: `sota_freight_advanced_v2.menu_freight_ar_invoice_line`)
    - **Tuổi nợ phải thu** (ID: 357, Action: 495, XML: `to_account_reports.aged_receivable_client_menu`)
    - **Tuổi nợ phải trả** (ID: 358, Action: 496, XML: `to_account_reports.aged_payable_client_menu`)
    - **Sổ Công Nợ một Khách hàng/Nhà cung cấp** (ID: 523, Action: 741, XML: `to_account_reports.menu_single_partner_ledger_report`)
    - **Sổ Công Nợ Theo Tài Khoản** (ID: 524, Action: 742, XML: `to_account_reports.menu_account_based_partner_ledger_report`)
    - **Công Nợ Phải Thu - Phải Trả** (ID: 595, Action: 869, XML: `sota_freight_advanced.menu_debt_ar_ap_report`)
  - **Quản lý** (ID: 203, XML: `account.account_reports_management_menu`)
    - **Phân tích Hoá đơn** (ID: 204, Action: 325, XML: `account.menu_action_account_invoice_report_all`)
    - **Daily Cash Flow** (ID: 553, Action: 773, XML: `to_account_reports.daily_cash_flow_client_menu`)
    - **Phân tích kết chuyển / phân bổ** (ID: 337, Action: 466, XML: `viin_account.menu_account_transfer_allocation`)
    - **Tài sản** (ID: 560, Action: 782, XML: `sota_account_asset.menu_action_asset_asset_report`)
    - **Tài sản cố định** (ID: 561, Action: 787, XML: `sota_account_asset.menu_action_fixed_asset_report`)
  - **Bảng kê hóa đơn** (ID: 359, XML: `l10n_vn_viin_account_reports.invoice_declaration_vn_statements_menu`)
    - **Bảng kê hóa đơn, chứng từ bán ra (01 -1/GTGT)** (ID: 365, Action: 892, XML: `l10n_vn_viin_account_reports.l10n_vn_c119_01gtgt_menu`)
    - **Bảng kê hóa đơn, chứng từ mua vào (01 - 2/GTGT)** (ID: 366, Action: 893, XML: `l10n_vn_viin_account_reports.l10n_vn_c119_02gtgt_menu`)
  - **Báo cáo kế toán Việt Nam - xem trước** (ID: 604, XML: `to_account_reports.vn_accounting_reports_preview_root_menu`)
    - **Sổ nhật ký chung (S03a-DN)** (ID: 605, Action: 882, XML: `to_account_reports.general_journal_client_menu`)
    - **Sổ cái (S03b-DN)** (ID: 606, Action: 883, XML: `to_account_reports.ledger_report_client_menu`)
    - **Sổ quỹ tiền mặt (S07-DN)** (ID: 607, Action: 884, XML: `to_account_reports.cash_book_client_menu`)
    - **Sổ tiền gửi ngân hàng (S08-DN)** (ID: 608, Action: 885, XML: `to_account_reports.bank_deposit_client_menu`)
    - **Sổ chi tiết tài khoản (S38-DN)** (ID: 609, Action: 886, XML: `to_account_reports.account_detail_sheet_client_menu`)
- **Cấu hình** (ID: 206, XML: `account.menu_finance_configuration`)
  - **Thiết lập** (ID: 207, Action: 328, XML: `account.menu_account_config`)
  - **Lên hóa đơn** (ID: 208, XML: `account.account_invoicing_menu`)
    - **Các điều khoản thanh toán** (ID: 209, Action: 318, XML: `account.menu_action_payment_term_form`)
    - **Điều khoản thương mại** (ID: 210, Action: 337, XML: `account.menu_action_incoterm_open`)
  - **Ngân hàng** (ID: 211, XML: `account.account_banks_menu`)
    - **Thêm tài khoản ngân hàng** (ID: 212, Action: 320, XML: `account.menu_action_account_bank_journal_form`)
    - **Đối tượng đối soát** (ID: 213, Action: 315, XML: `account.action_account_reconcile_model_menu`)
  - **Kế toán** (ID: 214, XML: `account.account_account_menu`)
    - **Hệ thống tài khoản** (ID: 215, Action: 309, XML: `account.menu_action_account_form`)
    - **Thuế** (ID: 216, Action: 316, XML: `account.menu_action_tax_form`)
    - **Các sổ nhật ký** (ID: 217, Action: 311, XML: `account.menu_action_account_journal_form`)
    - **Tiền tệ** (ID: 219, Action: 67, XML: `account.menu_action_currency_form`)
    - **Vị thế tài chính** (ID: 220, Action: 330, XML: `account.menu_action_account_fiscal_position_form`)
    - **Nhóm sổ nhật ký** (ID: 221, Action: 312, XML: `account.menu_action_account_journal_group_list`)
  - **Thanh toán** (ID: 223, XML: `account.root_payment_menu`)
    - **Các nhà cung cấp thanh toán** (ID: 293, Action: 264, XML: `account_payment.payment_provider_menu`)
  - **Quản lý** (ID: 224, XML: `account.account_management_menu`)
    - **Nhóm sản phẩm** (ID: 225, Action: 215, XML: `account.menu_product_product_categories`)
    - **Làm tròn tiền** (ID: 226, Action: 326, XML: `account.menu_action_rounding_form_view`)
    - **Nhóm Tài sản** (ID: 558, Action: 780, XML: `sota_account_asset.account_asset_category_purchase_menu`)
    - **Các quy tắc kết chuyển** (ID: 570, Action: 806, XML: `sota_account_closing_entry_forward.account_balance_carry_forward_rule_menu`)
  - **Vietnam E-invoice** (ID: 562, XML: `sota_vn_edi.menu_vn_einvoice_root`)
    - **E-Invoice Provider** (ID: 563, Action: 794, XML: `sota_vn_edi.menu_einvoice_provider`)
    - **E-Invoice Serial** (ID: 564, Action: 795, XML: `sota_vn_edi.menu_einvoice_serial`)
    - **E-Invoice Template** (ID: 566, Action: 797, XML: `sota_vn_edi.menu_einvoice_template`)
    - **E-Invoice Type** (ID: 565, Action: 796, XML: `sota_vn_edi.menu_einvoice_type`)
  - **Kế toán phân tích** (ID: 227, XML: `account.menu_analytic_accounting`)
    - **Mô hình phân bổ phân tích** (ID: 228, Action: 177, XML: `account.menu_analytic__distribution_model`)
    - **Các tài khoản phân tích** (ID: 229, Action: 175, XML: `account.account_analytic_def_account`)
    - **Kế hoạch phân tích** (ID: 230, Action: 176, XML: `account.account_analytic_plan_menu`)
    - **Thẻ TK quản trị** (ID: 338, Action: 467, XML: `viin_analytic_tag.account_analytic_tag_menu`)

---

## 📦 Module: Email Marketing
- **ID:** 255 | **Action:** 385 | **XML ID:** `mass_mailing.mass_mailing_menu_root`

### Các Menu con (Submenus / Features):
- **Mailings** (ID: 256, Action: 385, XML: `mass_mailing.mass_mailing_menu`)
- **Danh sách liên hệ** (ID: 257, XML: `mass_mailing.mass_mailing_mailing_list_menu`)
  - **Danh sách liên hệ** (ID: 258, Action: 384, XML: `mass_mailing.menu_email_mass_mailing_lists`)
  - **Liên hệ của danh sách liên hệ** (ID: 259, Action: 383, XML: `mass_mailing.menu_email_mass_mailing_contacts`)
- **Chiến dịch** (ID: 260, Action: 390, XML: `mass_mailing.menu_email_campaigns`)
- **Báo cáo** (ID: 261, Action: 379, XML: `mass_mailing.menu_mass_mailing_report`)
- **Cấu hình** (ID: 262, XML: `mass_mailing.mass_mailing_configuration`)
  - **Thiết lập** (ID: 263, Action: 389, XML: `mass_mailing.menu_mass_mailing_global_settings`)
  - **Các giai đoạn của chiến dịch** (ID: 264, Action: 170, XML: `mass_mailing.menu_view_mass_mailing_stages`)
  - **Thẻ chiến dịch** (ID: 265, Action: 171, XML: `mass_mailing.mass_mailing_tag_menu`)
  - **Kiểm soát đường dẫn** (ID: 266, Action: 205, XML: `mass_mailing.link_tracker_menu_mass_mailing`)
  - **Địa chỉ email bị liệt vào danh sách đen** (ID: 267, Action: 123, XML: `mass_mailing.mail_blacklist_mm_menu`)
  - **Bộ lọc yêu thích** (ID: 268, Action: 380, XML: `mass_mailing.mailing_filter_menu_action`)

---

## 📦 Module: Nhân viên
- **ID:** 136 | **Action:** 193 | **XML ID:** `hr.menu_hr_root`

### Các Menu con (Submenus / Features):
- **Nhân viên** (ID: 138, XML: `hr.menu_hr_employee_payroll`)
  - **Nhân viên** (ID: 139, Action: 193, XML: `hr.menu_hr_employee_user`)
  - **Hợp đồng** (ID: 162, Action: 238, XML: `hr_contract.hr_menu_contract_history`)
- **Phòng/Ban** (ID: 146, Action: 198, XML: `hr.menu_hr_department_kanban`)
- **Cấu hình** (ID: 143, XML: `hr.menu_human_resources_configuration`)
  - **Thiết lập** (ID: 155, Action: 201, XML: `hr.hr_menu_configuration`)
  - **Nhân viên** (ID: 144, XML: `hr.menu_config_employee`)
    - **Phòng/Ban** (ID: 145, Action: 199, XML: `hr.menu_hr_department_tree`)
    - **Vị trí làm việc** (ID: 147, Action: 200, XML: `hr.menu_hr_work_location_tree`)
    - **Lý do nghỉ việc** (ID: 148, Action: 185, XML: `hr.menu_hr_departure_reason_tree`)
  - **Tuyển dụng** (ID: 150, XML: `hr.menu_config_recruitment`)
    - **Vị trí công việc** (ID: 151, Action: 187, XML: `hr.menu_view_hr_job`)
    - **Loại việc làm** (ID: 152, Action: 186, XML: `hr.menu_view_hr_contract_type`)
  - **Kế hoạch hoạt động** (ID: 153, XML: `hr.menu_config_plan`)
    - **Xử lý vào làm/thôi việc** (ID: 154, Action: 188, XML: `hr.menu_config_plan_plan`)

---

## 📦 Module: Tạm ứng Nhân viên
- **ID:** 495 | **Action:** 704 | **XML ID:** `to_hr_employee_advance.employee_advance_menu_root`

### Các Menu con (Submenus / Features):
- **Đề nghị/Khai báo** (ID: 496, XML: `to_hr_employee_advance.employee_advance_menu`)
  - **Đề nghị/Khai báo** (ID: 499, Action: 704, XML: `to_hr_employee_advance.employee_advance_menu_request`)
  - **Chờ duyệt** (ID: 500, Action: 705, XML: `to_hr_employee_advance.employee_advance_menu_to_approve`)
  - **Đã phê duyệt** (ID: 501, Action: 706, XML: `to_hr_employee_advance.employee_advance_menu_approved`)
  - **Đã thanh toán** (ID: 502, Action: 707, XML: `to_hr_employee_advance.employee_advance_menu_paid`)
  - **Đã đối soát** (ID: 503, Action: 708, XML: `to_hr_employee_advance.employee_advance_menu_reconciled`)
- **Kế toán** (ID: 497, XML: `to_hr_employee_advance.employee_advance_menu_accounting`)
  - **Đối soát tạm ứng** (ID: 505, Action: 710, XML: `to_hr_employee_advance.employee_advance_reconcile_menu`)
  - **Đối soát hàng loạt** (ID: 498, Action: 703, XML: `to_hr_employee_advance.employee_advance_reconcile_batch_menu`)
- **Báo cáo** (ID: 504, Action: 709, XML: `to_hr_employee_advance.employee_advance_menu_report`)
- **Cấu hình** (ID: 506, XML: `to_hr_employee_advance.employee_advance_menu_configuration`)
  - **Thiết lập** (ID: 507, Action: 711, XML: `to_hr_employee_advance.employee_advance_menu_general_settings`)

---

## 📦 Module: Chi phí
- **ID:** 297 | **Action:** 421 | **XML ID:** `hr_expense.menu_hr_expense_root`

### Các Menu con (Submenus / Features):
- **Chi phí của tôi** (ID: 298, XML: `hr_expense.menu_hr_expense_my_expenses`)
  - **Chi phí của tôi** (ID: 299, Action: 421, XML: `hr_expense.menu_hr_expense_my_expenses_all`)
  - **Kê khai của Tôi** (ID: 300, Action: 423, XML: `hr_expense.menu_hr_expense_sheet_my_reports`)
- **Kê khai chi phí** (ID: 301, Action: 424, XML: `hr_expense.menu_hr_expense_report`)
- **Báo cáo** (ID: 302, XML: `hr_expense.menu_hr_expense_reports`)
  - **Phân tích Chi phí** (ID: 303, Action: 420, XML: `hr_expense.menu_hr_expense_all_expenses`)
- **Cấu hình** (ID: 304, XML: `hr_expense.menu_hr_expense_configuration`)
  - **Thiết lập** (ID: 308, Action: 431, XML: `hr_expense.menu_hr_expense_global_settings`)
  - **Danh mục chi phí** (ID: 305, Action: 422, XML: `hr_expense.menu_hr_product`)

---

## 📦 Module: Thiết lập
- **ID:** 4 | **Action:** 85 | **XML ID:** `base.menu_administration`

### Các Menu con (Submenus / Features):
- **Thiết lập chung** (ID: 70, Action: 85, XML: `base_setup.menu_config`)
- **Người dùng & Công ty** (ID: 7, XML: `base.menu_users`)
  - **Người dùng** (ID: 64, Action: 70, XML: `base.menu_action_res_users`)
  - **Công ty** (ID: 61, Action: 53, XML: `base.menu_action_res_company_form`)
  - **Login Details** (ID: 69, Action: 79, XML: `login_user_detail.menu_1_list`)
  - **Roles** (ID: 106, Action: 154, XML: `base_user_role.menu_action_res_users_role_tree`)
- **System Usage** (ID: 581, XML: `sota_system_usage.menu_system_usage`)
  - **OCR Usage Log** (ID: 580, Action: 841, XML: `sota_freight_advanced.menu_freight_ocr_log`)

---

