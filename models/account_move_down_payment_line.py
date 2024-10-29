from odoo import models, api, fields

class AccountMoveDownPaymentLine(models.Model):
    _name = 'account.move.down.payment.line'
    _description = 'Down Payment Product Line'

    move_id = fields.Many2one('account.move', string='Invoice', ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Char(string='Description')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    company_id = fields.Many2one('res.company', string='Company', related='move_id.company_id', store=True)