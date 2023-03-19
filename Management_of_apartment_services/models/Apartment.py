from odoo import fields, models, api

class Apartment(models.Model):
    _name = 'apartment'
    _description = 'Thông tin căn hộ'
    _rec_name = 'roomnumber'
    _sql_constraints = [
        ('roomnumber_unique', 'unique(roomnumber)', 'Căn hộ đã được nhập thông tin')
    ]

    roomnumber = fields.Integer(string="Số phòng", required=True)
    roomarea = fields.Integer(string="Diện tích", required=True)
    roomfloor = fields.Integer(string="Tầng", compute='_get_floor', store=True)
    roomdesc = fields.Text(string="Mô tả căn hộ")
    roomimage = fields.Binary(string="Hình ảnh căn hộ")
    roomrating = fields.Selection([('0', '0'), ('1', 'Rất kém'), ('2', 'Kém'), ('3', 'Trung bình'), ('4', 'Tốt'), ('5', 'Rất tốt')], string="Tình trạng căn hộ")
    roomstatus = fields.Selection([('off', 'Vẫn còn trống'), ('on', 'Đã có người cư trú')], string="Trạng thái", default='off')

    @api.depends('roomnumber')
    def _get_floor(self):
        for Apartment in self:
            Apartment.roomfloor = Apartment.roomnumber // 100

    @api.onchange('roomrating')
    def onchange_roomrating(self):
        if self.roomrating:
            if self.roomrating == '1':
                return {'warning':
                    {
                        'title': 'Cảnh báo tình trạng căn hộ',
                        'message': 'Căn hộ đang trong tình trạng rất kém.\n'
                                   'Ban quản lý nên có kế hoạch tu sửa'
                    }}