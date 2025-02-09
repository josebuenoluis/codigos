# -*- coding: utf-8 -*-
{
    'name': "FCTIES",

    'summary': "Gestión del alumnado en prácticas de FCT y empresas colaboradoras.",

    'description': """
Este módulo permite gestionar la información del
alumnado de Formación en Centros de Trabajo (FCT), 
incluyendo sus datos personales, la empresa 
donde realizan sus prácticas y el período de formación. 
    """,

    'author': "Jose Francisco Bueno Luis",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

