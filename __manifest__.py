# -*- coding: utf-8 -*-
{
    "license": "LGPL-3",
    'name': "test_cicd",
    'author': "Anderson",
    'website': "https://github.com/actonsys",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '15.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'views/views_res_partner.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
