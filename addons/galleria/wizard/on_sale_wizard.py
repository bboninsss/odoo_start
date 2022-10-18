# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError


class on_sale_wizard(models.TransientModel):
    _name="on_sale_wizard"
    _description="on_sale"


    name=fields.Many2one("galleria_opera", string="Nome Opera")
    code=fields.Char(string="CodiceID", related="name.idcode")
    sale_artist=fields.Many2one(related="name.artista", string="Artista")
    list_price=fields.Float(string="prezzo")
    exclusive=fields.Selection(string="Esclusività", related="name.exclusive")


    def action_on_sale(self):
        vals= {
        'name':self.name.id,
        'code':self.code,
        'list_price':self.list_price,
        'exclusive':self.exclusive
        }
        self.env['product.template'].create(vals)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            opera = self.env['product.template'].search([('name', '=', self.name.id), ('id', '!=', rec.id)])
            if opera:
                raise ValidationError(_("Il prodotto è già in vendita"))


