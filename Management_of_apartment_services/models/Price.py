from odoo import fields, models, api

class Price(models.Model):
    _name = 'price'
    _description = 'Cập nhật giá dịch vụ'
    _rec_name = 'dateprice'

    dateprice = fields.Datetime(string='Ngày cập nhật giá', required=True)

    waterprice= fields.Integer(string="Giá nước", default=9000)
    electricprice = fields.Integer(string="Giá điện", default=4000)
    veh1 = fields.Integer(string='Giá gửi xe ô tô', default=2400000)
    veh2 = fields.Integer(string='Giá gửi xe máy', default=60000)
    veh3 = fields.Integer(string='Giá gửi xe đạp', default=30000)

    pub = fields.Integer(string='Giá dịch vụ chung/m2', default=3000)

    last_price_id = fields.Integer(compute='_get_id', store=True)
    @api.depends('dateprice')
    def _get_id(self):
        for Price in self:
            Price.last_price_id = self.env['price'].search([])[-1].id

    last_price_veh1 = fields.Integer(compute='_get_veh1', store=True)
    @api.depends('dateprice')
    def _get_veh1(self):
        for Price in self:
            Price.last_price_veh1 = self.env['price'].search([])[-1].veh1

    last_price_veh2 = fields.Integer(compute='_get_veh2', store=True)
    @api.depends('dateprice')
    def _get_veh2(self):
        for Price in self:
            Price.last_price_veh2 = self.env['price'].search([])[-1].veh2

    last_price_veh3 = fields.Integer(compute='_get_veh3', store=True)
    @api.depends('dateprice')
    def _get_veh3(self):
        for Price in self:
            Price.last_price_veh3 = self.env['price'].search([])[-1].veh3

    last_price_pub = fields.Integer(compute='_get_pub', store=True)
    @api.depends('dateprice')
    def _get_pub(self):
        for Price in self:
            Price.last_price_pub = self.env['price'].search([])[-1].pub

    last_price_water = fields.Integer(compute='_get_waterprice', store=True)
    @api.depends('dateprice')
    def _get_waterprice(self):
        for Price in self:
            Price.last_price_water = self.env['price'].search([])[-1].waterprice

    last_price_electric = fields.Integer(compute='_get_electricprice', store=True)
    @api.depends('dateprice')
    def _get_electricprice(self):
        for Price in self:
            Price.last_price_electric = self.env['price'].search([])[-1].electricprice