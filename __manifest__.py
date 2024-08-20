{
    'name': 'Custom Down Payment',
    'version': '1.1.7',
    'summary': 'Custom module to include products in down payment invoices',
    'description': """This module modifies the down payment invoices to include products.""",
    'author': 'Your Name',
    'category': 'Accounting',
    'depends': ['account', 'sale', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
