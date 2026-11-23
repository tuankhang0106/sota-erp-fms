# -*- coding: utf-8 -*-
{
    'name': 'Thiết lập (Settings & Administration)',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Cloned Module for Thiết lập (Settings & Administration)',
    'description': """Thiết lập (Settings & Administration) cloned from SotaERP Portalink""",
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'data/base_setup_data.xml',
        'views/res_company_views.xml',
        'views/res_users_views.xml',
        'views/login_detail_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_users_role_views.xml',
        'views/freight_ocr_log_views.xml',
        'views/base_setup_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
