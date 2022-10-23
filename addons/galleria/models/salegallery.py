# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import date


class salegallery(models.Model):
    _inherit="product.template"
    name=fields.Many2one("galleria_opera", string="Opera")
    code=fields.Char(string="CodiceID", related="name.idcode")
    sale_artist=fields.Many2one(related="name.artista", string="Artista")
    opera_data=fields.Date(string="Data produzione",related="name.data")
    tipo_opera=fields.Selection(string="Tipologia", related="name.tipo_opera")
    exclusive=fields.Selection(string="Esclusività",related="name.exclusive")
    opera_image=fields.Image(string="immagine", related="name.opera_image")
    opera_description=fields.Text(string="Descrizione",related="name.opera_description")
    

