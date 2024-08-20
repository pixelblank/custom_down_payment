from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _create_invoices(self, grouped=False, final=False):
        invoices = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final)
        for invoice in invoices:
            if invoice.move_type == 'out_invoice' and self.env.context.get('down_payment_mode'):
                invoice.write({'is_down_payment': True})
        return invoices

    def _get_invoice_grouping_keys(self):
        res = super(SaleOrder, self)._get_invoice_grouping_keys()
        res.append('is_down_payment')
        return res