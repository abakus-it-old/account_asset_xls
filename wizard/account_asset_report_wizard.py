# -*- encoding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import MissingError
from openerp.tools.translate import _

class wiz_account_asset_report(models.TransientModel):
    _name = 'wiz.account.asset.report'
    _description = 'Financial Assets report'

    def compute_default_company_id(self):
        return self.env['res.users'].browse(self.env.uid).company_id.id
    
    date_start = fields.Date(string='Date start', required=True)
    date_end = fields.Date(string='Date end', required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', required=True, default=compute_default_company_id)
    
    @api.multi
    def xls_export(self):
        if self.env['account.asset.asset'].search_count([('company_id', '=', self.company_id.id)]) == 0:
            raise MissingError(_("No assets found for your selection!"))
     
        datas = {
            'model': 'account.asset.asset',
            'date_start': self.date_start,
            'date_end': self.date_end,
            'company_id': self.company_id.id
        }

        return {'type': 'ir.actions.report.xml',
                'report_name': 'account.asset.xls',
                'datas': datas}
                