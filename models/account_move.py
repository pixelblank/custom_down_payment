from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    product_names = fields.Text(string="Product Names", compute='_compute_product_names', store=True)
    debug_info = fields.Text(string="Order Lines Summary", compute='_compute_debug_info')

    @api.depends('invoice_line_ids', 'invoice_origin')
    def _compute_product_names(self):
        for move in self:
            if move.invoice_origin:
                sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)
                if sale_order:
                    product_names = []
                    for line in sale_order.order_line:
                        product_names.append(f"{line.product_id.name}: {line.product_uom_qty} x {line.price_unit}")
                    move.product_names = "\n".join(product_names)
                else:
                    move.product_names = "No sale order found"
            else:
                move.product_names = "Not a down payment invoice"

    @api.depends('invoice_line_ids', 'invoice_origin')
    def _compute_debug_info(self):
        for move in self:
            debug_info = []
            debug_info.append(f"Move ID: {move.id}")
            debug_info.append(f"Invoice Origin: {move.invoice_origin}")

            if move.invoice_origin:
                sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)
                if sale_order:
                    debug_info.append(f"Sale Order found: {sale_order.name}")
                    debug_info.append(f"Sale Order lines: {len(sale_order.order_line)}")
                    for line in sale_order.order_line:
                        debug_info.append(f"- {line.product_id.name}: {line.product_uom_qty} x {line.price_unit}")
                else:
                    debug_info.append("No Sale Order found")

            debug_info.append(f"Invoice lines: {len(move.invoice_line_ids)}")
            for line in move.invoice_line_ids:
                debug_info.append(f"- {line.product_id.name}: {line.quantity} x {line.price_unit}")

            move.debug_info = "\n".join(debug_info)