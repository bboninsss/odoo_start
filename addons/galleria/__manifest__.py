# -*- coding: utf-8 -*-
{
    'name': "galleria",

    'summary': """
        custom module for sia project:"Arte31" """,

    'description': """
        Long description of module's purpose
    """,

    'author': "bboninsss",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        #'views/views.xml',
        #'views/templates.xml',
        'views/galleria_opera.xml',
        'views/artista.xml',
        'views/salegallery.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,

}
