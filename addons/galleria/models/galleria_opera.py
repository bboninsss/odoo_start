# -*- coding: utf-8 -*-

from odoo import models, fields, api 
from datetime import date


class galleria_opera(models.Model):
    _name="galleria_opera"
    _description="opera"
    _recname="code"

    code=fields.Char(string="CodiceID", readonly=True, 
            default='New')
    name=fields.Char(string="Nome Opera")
    autore=fields.Char(string="Autore")
    data=fields.Date(string="Data produzione")
    opera_type=fields.Selection([('Dipinto', 'Dipinto'),('scultura','Scultura')], string="Tipologia", default='Dipinto')
    opera_image=fields.Image(string="immagine", max_width=200, max_height=200)
    opera_description=fields.Html(string="Descrizione")