from odoo import models, fields, api

class Service(models.Model):

    _name = 'service'

    _description = 'Dịch vụ'
    _rec_name = 'servicecode'
    _sql_constraints = [
        ('service_unique', 'unique(servicecode)', 'Mã dịch vụ đã được tạo')
    ]

    servicecode = fields.Char(string="Mã dịch vụ", required=True)

    customer_id = fields.Many2one(comodel_name='customer', string='Căn hộ', required=True)

    #Water Service
    waterqtt = fields.Integer(string='Số nước', required=True)
    waterinvoice = fields.Integer(string='Tiền nước', compute='_get_water', store=True)

    #Electric Service
    electricqtt = fields.Integer(string='Số điện', required=True)
    electricinvoice = fields.Integer(string='Tiền điện', compute='_get_electric', store=True)

    #Parking Service
    car = fields.Integer(related='customer_id.numcar', string='Ô tô')
    motorbike = fields.Integer(related='customer_id.nummotor', string='Xe máy')
    bike = fields.Integer(related='customer_id.numbike', string='Xe đạp')
    parkinginvoice = fields.Integer(string='Tiền gửi xe', compute='_get_parking', store=True)

    #General Service
    publicqtt = fields.Integer(related='customer_id.area', store=True)
    publicinvoice = fields.Integer(string='Dịch vụ chung', compute='_get_public', store=True)

    last_price = fields.Many2one(comodel_name='price', string="Ngày cập nhật giá", required=True)
    last_price_watersv = fields.Integer(related='last_price.last_price_water')
    last_price_electricsv = fields.Integer(related='last_price.last_price_electric')


    svve1 = fields.Integer(related='last_price.last_price_veh1')
    svve2 = fields.Integer(related='last_price.last_price_veh2')
    svve3 = fields.Integer(related='last_price.last_price_veh3')

    svpub = fields.Integer(related='last_price.last_price_pub')

    @api.depends('waterqtt')
    def _get_water(self):
        for Service in self:
            Service.waterinvoice = Service.waterqtt * Service.last_price_watersv

    @api.depends('electricqtt')
    def _get_electric(self):
        for Service in self:
            Service.electricinvoice = Service.electricqtt * Service.last_price_electricsv

    @api.depends('car', 'motorbike', 'bike')
    def _get_parking(self):
        for Service in self:
            Service.parkinginvoice = Service.svve1 * Service.car + Service.svve2 * Service.motorbike + Service.svve3 * Service.bike


    @api.depends('publicqtt')
    def _get_public(self):
        for Service in self:
            Service.publicinvoice = Service.publicqtt * Service.svpub


    @api.onchange('waterqtt')
    def onchange_waterqtt(self):
        if self.waterqtt:
            if self.waterqtt > 50:
                return {'warning':
                            {
                                'title': 'Cảnh báo mức tiêu thụ nước',
                                'message': 'Mức tiêu thụ nước vượt quá bình thường.\n'
                                            'Vui lòng liên hệ chủ căn hộ và kỹ thuật để kiểm tra lại đồng hồ nước'
                            }}

    @api.onchange('electricqtt')
    def onchange_electricqtt(self):
        if self.electricqtt:
            if self.electricqtt > 500:
                return {'warning':
                    {
                        'title': 'Cảnh báo mức tiêu thụ điện',
                        'message': 'Mức tiêu thụ điện vượt quá bình thường.\n'
                                   'Vui lòng liên hệ chủ căn hộ và kỹ thuật để kiểm tra lại công tơ điện'
                    }}






