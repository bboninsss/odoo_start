# -*- coding: utf-8 -*-

from odoo import models, fields, api 
from datetime import date


class salegallery(models.Model):
    _inherit="product.template"
    name=fields.Many2one("galleria_opera", string="Opera")
    code=fields.Char(string="CodiceID", related="name.idcode")
    sale_artist=fields.Many2one(related="name.artista", string="Artista")
    opera_data=fields.Date(string="Data produzione",related="name.data")
    opera_type=fields.Selection([('Dipinto','Dipinto'),('Scultura','Scultura')], string="Tipologia", related="name.opera_type")
    exclusive=fields.Boolean(string="Exclusive",related="name.exclusive")
    opera_image=fields.Image(string="immagine", max_width=100, max_height=100, widget="image", related="name.opera_image")
    opera_description=fields.Char(string="Descrizione",related="name.opera_description")
