from odoo import models, api, fields
import logging

# Initialiser le logger pour ce module
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    # Hériter du modèle account.move
    _inherit = 'account.move'

    down_payment_product_lines = fields.One2many('account.move.down.payment.line', 'move_id', string="Down Payment Product Lines")


    @api.model
    def create(self, vals):
        move = super(AccountMove, self).create(vals)

        if move.move_type == 'out_invoice' and move.invoice_origin:
            sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)

            if sale_order:
                is_down_payment = any(line.is_downpayment for line in sale_order.order_line)

                if is_down_payment:
                    for line in sale_order.order_line:
                        if line.product_id and not line.is_downpayment:
                            self.env['account.move.down.payment.line'].create({
                                'move_id': move.id,
                                'product_id': line.product_id.id,
                                'name': line.product_id.name,
                                'quantity': line.product_uom_qty,
                                'price_unit': line.price_unit,
                            })

                    down_payment_product_lines = fields.One2many('account.move.down.payment.line', 'move_id', string="Down Payment Product Lines")
                    _logger.info('Down payment lines saved: %s', move.down_payment_product_lines)


        return move
