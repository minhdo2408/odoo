from odoo import fields, models, api


class Datetopaid(models.TransientModel):
    _name = 'datetopaid'
    _description = ''

    datetopaid = fields.Date(string='Ngày thanh toán')

    def action_confirm(self):
        bill_id = self.env.context.get('active_id', False)
        bill = self.env['bill'].browse(bill_id)
        bill.write({'paiddate': self.datetopaid})
        bill.to_paid()
