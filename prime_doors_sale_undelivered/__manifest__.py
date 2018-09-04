{
    'name': 'Prime Doors Sales Undelivered',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'version': '11.0.1.0.0',
    'category': 'Sales',
    'sequence': 95,
    'summary': 'Undelivered Sales',
    'description': """
Adds columns and reports to determine unshipped/unearned totals.
    """,
    'website': 'https://hibou.io/',
    'depends': [
        'sale_stock',
    ],
    'data': [
        'views/sale_views.xml',
    ],
    'installable': True,
    'application': False,
}
