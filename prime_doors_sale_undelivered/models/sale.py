from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    percent_delivered = fields.Float('Delivered (%)', compute='_compute_percent_delivered', store=True)
    amount_not_delivered = fields.Monetary('Amount not Delivered', compute='_compute_percent_delivered', store=True)

    @api.multi
    @api.depends('order_line.product_uom_qty', 'order_line.qty_delivered', 'order_line.price_unit')
    def _compute_percent_delivered(self):
        for order in self:
            qty_ordered = 0.0
            qty_delivered = 0.0
            amount_undelivered = 0.0
            for line in order.order_line:
                qty_ordered += line.product_uom_qty
                qty_delivered += line.qty_delivered
                amount_undelivered += line.price_unit * (line.product_uom_qty - line.qty_delivered)

            order.percent_delivered = (qty_delivered / qty_ordered) * 100.0 if qty_ordered != 0.0 else -1
            order.amount_not_delivered = amount_undelivered
