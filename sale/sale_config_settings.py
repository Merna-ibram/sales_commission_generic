from odoo import api, fields, models

class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    commission_configuration = fields.Selection([
        ('sale_order', 'Commission based on sales order'),
        ('invoice', 'Commission based on invoice'),
        ('payment', 'commission based on payment')
    ], string='Generate Commission Entry Based On', default='payment')

    commission_discount_account = fields.Many2one(
        'account.account',
        domain=[('account_type', '=', 'expense')],
        string="Commission Account"
    )


class SaleConfigurationSettings(models.TransientModel):
    _inherit = "res.config.settings"

    commission_configuration = fields.Selection(
        string='Generate Commission Entry Based On',
        related="company_id.commission_configuration",
        readonly=False
    )

    commission_discount_account = fields.Many2one(
        'account.account',
        domain=[('account_type', '=', 'expense')],
        string="Commission Account",
        related="company_id.commission_discount_account",
        readonly=False
    )
