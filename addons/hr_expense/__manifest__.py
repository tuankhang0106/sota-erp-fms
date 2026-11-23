# -*- coding: utf-8 -*-
{
    'name': 'Chi phí (Expenses)',
    'version': '1.0',
    'category': 'Human Resources/Expenses',
    'summary': 'Cloned Module for Chi phí (Expenses)',
    'description': """Chi phí (Expenses) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base","mail","account"],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_expense_data.xml',
        'views/hr_expense_views.xml',
        'views/product_product_views.xml',
        'views/hr_expense_sheet_views.xml',
        'views/res_config_settings_views.xml',
        'views/hr_expense_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
