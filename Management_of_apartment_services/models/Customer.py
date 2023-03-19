from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'customer'
    _description = 'Thông tin khách hàng'
    _rec_name = 'apartment_id'
    _sql_constraints = [
        ('apartment_unique', 'unique(apartment_id)', 'Căn hộ hiện tại đã có người cư trú')
    ]

    apartment_id = fields.Many2one(comodel_name='apartment', string='Căn hộ', required=True, domain="[('roomstatus','=','off'), ('roomrating', '!=', '1')]")
    apartmentnumber = fields.Integer(related='apartment_id.roomnumber')
    floor = fields.Integer(related='apartment_id.roomfloor', string='Tầng', store=True)
    owner = fields.Char(string='Chủ sở hữu', required=True)
    gender = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    cmnd = fields.Char(string='CMND/CCCD', required=True)
    phone = fields.Char(string='Số điện thoại', trim=True, required=True)
    area = fields.Integer(related='apartment_id.roomarea', string='Diện tích')
    customerstatus = fields.Selection([('residing', 'Đang cư trú'), ('left', 'Đã rời đi')], string='Trạng thái khách hàng', default='residing')
    leavedate = fields.Date(string='Ngày rời đi', readonly=1)
    customerimage = fields.Binary(string="Cập nhật chân dung")

    vehicle_ids = fields.One2many(comodel_name='vehicle', inverse_name='owner_id')

    numcar = fields.Integer(compute='_count_car', store=True)
    nummotor = fields.Integer(compute='_count_motor', store=True)
    numbike = fields.Integer(compute='_count_bike', store=True)


    def to_leave(self):
        self.customerstatus = 'left'


    @api.constrains('phone')
    def validate_phone(self):
        for Customer in self:
            if Customer.phone and not Customer.phone.isnumeric():
                raise ValidationError('Vui lòng nhập lại số điện thoại!')


    @api.model
    def create(self, vals):
        if vals.get('owner', False):
            vals['owner'] = vals['owner'].title()
            record = super(Customer, self).create(vals)
        return record

    @api.depends('vehicle_ids')
    def _count_car(self):
        for Customer in self:
            Customer.numcar = self.env['vehicle'].search_count([('vehicleclass', '=', 'car'), ('owner_id', '=', self.id)])
            return Customer.numcar

    @api.depends('vehicle_ids')
    def _count_motor(self):
        for Customer in self:
            Customer.nummotor = self.env['vehicle'].search_count([('vehicleclass', '=', 'motorbike'), ('owner_id', '=', self.id)])
            return Customer.nummotor

    @api.depends('vehicle_ids')
    def _count_bike(self):
        for Customer in self:
            Customer.numbike = self.env['vehicle'].search_count([('vehicleclass', '=', 'bike'), ('owner_id', '=', self.id)])
            return Customer.numbike



