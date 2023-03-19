from odoo import fields, models, api

class Bill(models.Model):

    _name = 'bill'
    _description = 'Hóa đơn chi tiết'
    _rec_name = 'apartmentbill'
    _sql_constraints = [
        ('bill_unique', 'unique(service_id)', 'Hóa đơn đã được tạo')
    ]

    service_id = fields.Many2one(comodel_name='service', string='Mã dịch vụ', domain="[('customer_id', '=', csm_id)]", required=True)
    csm_id = fields.Many2one(comodel_name='customer', string='Căn hộ', required=True)

    date = fields.Date(string='Ngày lập hóa đơn', required=True)
    apartmentbill = fields.Integer(related='csm_id.apartmentnumber', string='Căn hộ')
    owerbill = fields.Char(related='csm_id.owner', string='Chủ căn hộ')


    waterbill = fields.Integer(related='service_id.waterinvoice', string='Hóa đơn nước')
    electricbill = fields.Integer(related='service_id.electricinvoice', string='Hóa đơn điện')
    parkingbill = fields.Integer(related='service_id.parkinginvoice', string='Hóa đơn gửi xe')
    publicbill = fields.Integer(related='service_id.publicinvoice', string='Hóa đơn dịch vụ chung')

    totalbill = fields.Integer(string='Hóa đơn tổng', compute='_get_total', store=True)

    billstatus = fields.Selection([('unpaid', 'Chưa thanh toán'), ('paid', 'Đã thanh toán')], string='Trạng thái hóa đơn', default='unpaid')
    paiddate = fields.Date(string='Ngày thanh toán', readonly=1)

    nbike = fields.Integer(related='service_id.bike')
    nmotorbike = fields.Integer(related='service_id.motorbike')
    ncar = fields.Integer(related='service_id.car')
    nwater = fields.Integer(related='service_id.waterqtt')
    nelectric = fields.Integer(related='service_id.electricqtt')
    narea = fields.Integer(related='csm_id.area')



    def to_paid(self):
        self.billstatus = 'paid'

    @api.depends('waterbill', 'electricbill', 'parkingbill', 'publicbill')
    def _get_total(self):
        for Bill in self:
            Bill.totalbill = Bill.waterbill + Bill.electricbill + Bill.parkingbill + Bill.publicbill