{
    'name': 'Custom Down Payment',
    'version': '1.2.1',  # Incrémentez la version
    'summary': 'Custom module to include products in down payment invoices',
    'description': """This module modifies the down payment invoices to include products.""",
    'author': 'Your Name',
    'category': 'Accounting',
    'depends': ['account', 'sale', 'sale_management', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'reports/invoice_report.xml',
        'reports/invoice_report_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
