# SotaERP / FMS Clone & Analysis Project

Hệ thống khảo sát, phân tích và tái tạo các module từ hệ thống SotaERP (Portalink FMS).

## Cấu trúc thư mục

- `addons/`: Chứa mã nguồn các module Odoo/FMS đã trích xuất và tái tạo (models, views, security, data) bao gồm:
  - `sota_freight_advanced`: Quản lý nghiệp vụ Vận tải & Logistics (Job, Master B/L, House B/L, SOA, Credit/Debit Note, P/L).
  - `account`: Nghiệp vụ Kế toán & Hóa đơn.
  - `crm`: Quản lý Khách hàng & Pipeline kinh doanh.
  - `contacts`: Danh bạ đối tác và chi tiết phân loại.
  - `hr`: Quản lý Nhân sự & Phòng ban.
  - `hr_expense`: Quản lý Chi phí.
  - `to_hr_employee_advance`: Quản lý Tạm ứng nhân viên.
  - `sh_activities_management`: Quản lý hoạt động & công việc.
  - `ks_dashboard_ninja`, `spreadsheet_dashboard`: Bảng điều khiển phân tích số liệu.
  - `mail`, `calendar`, `mass_mailing`, `base_setup`: Các phân hệ nền tảng.
- `survey_output/`: Tài liệu khảo sát chi tiết (danh mục menu, cấu trúc module, ảnh chụp màn hình).
- Các script phân tích, schema dữ liệu JSON phục vụ quá trình reverse-engineering và phát triển.

## Thiết lập môi trường

```bash
# Cài đặt dependencies Node.js (nếu chạy script khảo sát)
npm install
```
