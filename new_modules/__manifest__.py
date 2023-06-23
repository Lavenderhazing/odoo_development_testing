# -*- coding: utf-8 -*-
{
    'name': "new_modules",

    'summary': """
        This is a test module.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odessy Homer",
    'website': "http://www.odessyhomer.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/student_info_view.xml',
        'views/book_info_view.xml',
        'views/book_order_view.xml',
        'views/order_report_view.xml',
        'report/report_student_info.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
