# -*- coding: utf-8 -*-
{
    'name': "BusTrans",

    'summary': """
       BUS""",

    'description': """
       BUS
    """,

    'author': "Minds Solutions",
    'website': "http://www.mindseg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
'views/ir_ui_view.xml',
'views/ir_actions_act_window.xml',
        # 'security/ir.model.access.csv',
        'views/ir_ui_menu.xml',
   #     'views/templates.xml',
    #    'views/lov.xml',

      #  'views/ir_model_access.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo/demo.xml',
    ],
    'installable':True,
    'application': True,
}