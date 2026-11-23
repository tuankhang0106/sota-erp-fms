# -*- coding: utf-8 -*-
{
    'name': 'Discuss (Thảo luận)',
    'version': '1.0',
    'category': 'Productivity/Discuss',
    'summary': 'Chat, Channels, Mail and Activities Management',
    'description': """
Discuss and Messaging Module
============================
Cloned from SotaERP (Portalink)
- Chat Channels (Public, Private, Direct Messages)
- Messages & Notifications Stream
- Activity & Task Scheduling
- Document Followers & Chatter Mixin
    """,
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_data.xml',
        'views/mail_channel_views.xml',
        'views/mail_message_views.xml',
        'views/mail_activity_views.xml',
        'views/mail_activity_type_views.xml',
        'views/mail_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
