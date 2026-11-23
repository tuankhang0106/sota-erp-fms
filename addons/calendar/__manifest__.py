# -*- coding: utf-8 -*-
{
    'name': 'Calendar (Lịch)',
    'version': '1.0',
    'category': 'Productivity/Calendar',
    'summary': 'Schedule meetings, tasks and manage company calendar',
    'description': """
Calendar Module
===============
Cloned from SotaERP (Portalink)
- Schedule meetings, appointments and events
- Set email and popup alarms
- Manage attendees and RSVP status
- Synchronize with external calendar providers
    """,
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/calendar_data.xml',
        'views/calendar_event_views.xml',
        'views/calendar_alarm_views.xml',
        'views/calendar_event_type_views.xml',
        'views/calendar_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
