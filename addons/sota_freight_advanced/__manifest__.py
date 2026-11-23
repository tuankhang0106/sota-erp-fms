# -*- coding: utf-8 -*-
{
    'name': 'Freight Management System (Vận chuyển - FMS)',
    'version': '1.0',
    'category': 'Operations/Freight',
    'summary': 'International Freight Forwarding, Logistics, Job & Shipment Management (Sea, Air, Cross Border), SOA & Invoicing',
    'description': """
Freight Management System (FMS)
===============================
Cloned from SotaERP (Portalink)
- Comprehensive Freight Job Management (PLSE/PLAE/PLRD)
- House & Master B/L (Sea, Air, Cross Border)
- Freight Quotations & Sales Inquiries
- Debit Note, Credit Note, DC Note & SOA Debt Offset
- Logistics Master Data (Ports, Vessels, Airlines, Shipping Lines, Container Units, Incoterms, HS Codes)
- P/L Performance Reporting by Job, Salesman & Department
    """,
    'author': 'Cloned by Antigravity',
    'website': 'https://portalink.erp.sota-solutions.com/',
    'depends': ['base', 'mail', 'account'],
    'data': [
        'security/freight_security.xml',
        'security/ir.model.access.csv',
        'data/freight_data.xml',
        'views/freight_config_views.xml',
        'views/freight_job_views.xml',
        'views/freight_house_views.xml',
        'views/freight_master_views.xml',
        'views/freight_quotation_views.xml',
        'views/freight_financial_views.xml',
        'views/freight_pricing_views.xml',
        'views/freight_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
