from odoo import api, models, _

class SaleInvCommTemplate(models.AbstractModel):
    _name = 'report.sales_commission_generic.sale_inv_comm_template'
    _description = 'Report sale inv comm template'

    def _get_report_values(self, docids, data=None):
        record_ids = self.env[data['model']].browse(data['form'])  # دي المفروض ترجع recordset من نوع invoice.sale.commission

        return {
            'doc_ids': record_ids.ids,
            'doc_model': data['model'],
            'docs': record_ids,
            'data': data,
        }
