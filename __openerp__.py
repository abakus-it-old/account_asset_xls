# -*- encoding: utf-8 -*-

{
    'name': 'Assets Excel reporting',
    'version': '9.0.1.0',
    'license': 'AGPL-3',
    'author': "Bernard DELHEZ - AbAKUS it-solutions SARL",
    'category': 'Accounting & Finance',
    'description': """Assets Excel reporting

This module adds Excel reporting to Financial Assets Management Module.

This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions.
This module is inspired by the account_asset_management_xls module from Noviat and the Odoo Community Association (OCA).
    """,
    'depends': ['account_asset', 'report_xls'],
    'data': ['wizard/account_asset_report_wizard.xml',        
             'security/ir.model.access.csv',
            ],
    'installable': True,
}
