from odoo import api, fields, models, _

class ProductCategory(models.Model):
    _inherit = "product.category"

    total_sales = fields.Float(string='Achieved Amount', compute='_compute_total_sales')

    def _compute_total_sales(self):
        SaleOrderLine = self.env['sale.order.line']

        for category in self:
            # نجيب كل الـ sale order lines المرتبطة بالكاتيجوري أو أي سب-كاتيجوري ليها
            domain = [
                ('product_id.categ_id', 'child_of', category.id),
                ('order_id.state', 'not in', ['cancel']),
            ]
            order_lines = SaleOrderLine.search(domain)
            category.total_sales = sum(order_lines.mapped('price_total'))
