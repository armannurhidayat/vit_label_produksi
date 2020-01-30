# -*- coding: utf-8 -*-
{
    'name': "vit_label_produksi",

    'summary': """
        Printout label produksi
    """,

    'description': """
        Printout label produksi
    """,

    'author': "Arman Nur Hidayat <vitraining>",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mrp',
        'vit_mrp_cost',
        'stock',
        'vit_kartu_prod_add',
        'sale_purchase',
        'vit_package_master',
    ],

    # always loaded
    'data': [
        'report/label_produksi.xml',
    ],
}