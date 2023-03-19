from odoo import fields, models, api

class Vehicle(models.Model):
    _name = 'vehicle'
    _description = 'Quản lý phương tiện'
    _sql_constraints = [
        ('vehicleid_unique', 'unique(vehicleid)', 'Biển số xe đã tồn tại trong hệ thống')
    ]

    vehicleid = fields.Char(string='Số đăng ký xe')
    vehiclemodel = fields.Char(string='Kiểu xe', required=True)
    vehicleclass = fields.Selection([('car', 'Ô tô'), ('motorbike', 'Xe máy'), ('bike', 'xe đạp')], string='Loại xe')
    owner_id = fields.Many2one(comodel_name='customer', string='Căn hộ đăng ký gửi', required=True)
    vehicleimage = fields.Binary(string="Hình ảnh xe")