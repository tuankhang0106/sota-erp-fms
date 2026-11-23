# -*- coding: utf-8 -*-
{
    'name': 'Bảng điều khiển (Spreadsheet Dashboard)',
    'version': '1.0',
    'category': 'Productivity/Dashboards',
    'summary': 'Cloned Module for Bảng điều khiển (Spreadsheet Dashboard)',
    'description': """Bảng điều khiển (Spreadsheet Dashboard) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'data/spreadsheet_dashboard_data.xml',
        'views/spreadsheet_dashboard_group_views.xml',
        'views/spreadsheet_dashboard_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
