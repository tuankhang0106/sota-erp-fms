# -*- coding: utf-8 -*-
{
    'name': 'Activity Dashboard & Management',
    'version': '1.0',
    'category': 'Productivity/Activities',
    'summary': 'All Activities, My Activities, Supervisor View, Alarms, Tags and Dynamic Actions',
    'description': """
Activity Management & Dashboard Module
======================================
Cloned from SotaERP (Portalink)
- Activity Dashboard overview
- Supervisor Activities & Delegation
- My Activities & Team Reminders
- Dynamic Mass Actions
- Activity Tags and Custom Alarms
    """,
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/activity_data.xml',
        'views/sh_activity_tags_views.xml',
        'views/sh_activity_alarm_views.xml',
        'views/sh_activity_dynamic_action_views.xml',
        'views/mail_activity_views.xml',
        'views/res_config_settings_views.xml',
        'views/activity_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
