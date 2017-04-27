
{
    'name' : 'Journal Item Pivot View',
    'version' : '1.1',
    'summary': 'Journal Item Pivot View',
    'sequence': 30,
    'description': """
Technical Exam
----------------
Inheritance and application of pivot view on journal items (account.move.line)

created by: Romeo Abulencia (romeo@cloudemployee.co.uk)
    """,
    'category': 'Accounting custom module',
    'website': '',
    'images' : [],
    'depends' : ['account'],
    'data': [
        'views/account_view_inherit.xml',
    ],
    'demo': [
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
#    'post_init_hook': '',
}