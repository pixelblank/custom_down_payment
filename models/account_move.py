from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        move = super(AccountMove, self).create(vals)
        if move.move_type == 'out_invoice' and move.invoice_origin:
            sale_order = self.env['sale.order'].search([('name', '=', move.invoice_origin)], limit=1)
            if sale_order:
                for line in sale_order.order_line:
                    if line.product_id.name and not line.product_id.name.lower().startswith('acompte'):
                        self.env['account.move.line'].create({
                            'move_id': move.id,
                            'product_id': line.product_id.id,
                            'name': line.product_id.name,
                            'quantity': line.product_uom_qty,
                            'price_unit': line.price_unit,
                            'price_subtotal': line.price_unit * line.product_uom_qty,
                            'account_id': line.product_id.categ_id.property_account_income_categ_id.id,
                        })
        return move