# -*- coding: utf-8 -*-
{
    'name': 'Tạm ứng Nhân viên (Employee Advance)',
    'version': '1.0',
    'category': 'Human Resources/Advance',
    'summary': 'Cloned Module for Tạm ứng Nhân viên (Employee Advance)',
    'description': """Tạm ứng Nhân viên (Employee Advance) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base","mail","hr","account"],
    'data': [
        'security/ir.model.access.csv',
        'data/to_hr_employee_advance_data.xml',
        'views/employee_advance_reconcile_batch_views.xml',
        'views/employee_advance_views.xml',
        'views/employee_advance_reconcile_views.xml',
        'views/res_config_settings_views.xml',
        'views/to_hr_employee_advance_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
