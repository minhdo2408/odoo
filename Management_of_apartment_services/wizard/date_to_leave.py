from odoo import fields, models, api


class Datetoleave(models.TransientModel):
    _name = 'datetoleave'
    _description = ''

    datetoleave = fields.Date(string='Ngày rời đi')

    def action_confirm(self):
        customer_id = self.env.context.get('active_id', False)
        customer = self.env['customer'].browse(customer_id)
        customer.write({'leavedate': self.datetoleave})
        customer.to_leave()
