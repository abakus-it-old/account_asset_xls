# -*- encoding: utf-8 -*-

from openerp import models, api

class account_asset_asset(models.Model):
    _inherit = 'account.asset.asset'
    
    @api.model
    def _xls_acquisition_fields(self):
        """
        Update list in custom module to add/drop columns or change order
        """
        return ['account', 'name', 'code', 'date', 'value', 'salvage_value']

    @api.model
    def _xls_active_fields(self):
        """
        Update list in custom module to add/drop columns or change order
        """
        return [
            'account', 'name', 'code', 'date',
            'value', 'salvage_value',
            'fy_start_value', 'fy_depr', 'fy_end_value',
            'fy_end_depr',
            'method', 'method_number', 'prorata']
    
    @api.model
    def _xls_removal_fields(self):
        """
        Update list in custom module to add/drop columns or change order
        """
        return ['account', 'name', 'code', 'date', 'value', 'salvage_value']