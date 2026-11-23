# -*- coding: utf-8 -*-
{
    'name': 'My Dashboard (Dashboard Ninja)',
    'version': '1.0',
    'category': 'Productivity/Dashboards',
    'summary': 'Cloned Module for My Dashboard (Dashboard Ninja)',
    'description': """My Dashboard (Dashboard Ninja) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base","mail"],
    'data': [
        'security/ir.model.access.csv',
        'data/ks_dashboard_ninja_data.xml',
        'views/ks_dashboard_ninja_board_views.xml',
        'views/ks_dashboard_ninja_child_board_views.xml',
        'views/ks_dashboard_ninja_import_views.xml',
        'views/ks_dashboard_ninja_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
