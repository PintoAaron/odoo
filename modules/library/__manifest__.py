{
    'name': 'Library',
    'version': "17.0.1.0.0",
    'description': 'reading makes you brilliant',
    'application': True,
    'summary': 'Library Management System',
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
    'sequence': 15,
    'author': 'Pinto T. Aaron',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_user.xml',
    ],
    
}