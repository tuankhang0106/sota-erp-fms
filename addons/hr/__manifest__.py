# -*- coding: utf-8 -*-
{
    'name': 'Nhân viên (Human Resources)',
    'version': '1.0',
    'category': 'Human Resources/Employees',
    'summary': 'Cloned Module for Nhân viên (Human Resources)',
    'description': """Nhân viên (Human Resources) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base","mail"],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_data.xml',
        'views/hr_departure_reason_views.xml',
        'views/hr_contract_type_views.xml',
        'views/hr_job_views.xml',
        'views/hr_plan_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_department_views.xml',
        'views/hr_work_location_views.xml',
        'views/res_config_settings_views.xml',
        'views/hr_contract_history_views.xml',
        'views/hr_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
