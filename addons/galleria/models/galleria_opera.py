# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date


class galleria_opera(models.Model):
    _name="galleria_opera"
    _description="opera"
    _recname="idcode"

    idcode=fields.Char(string="CodiceID",required=True, readonly=True, default='New')
    name=fields.Char(string="Nome Opera")
    artista=fields.Many2one("artista", string="Artista")
    data=fields.Date(string="Data produzione")
    opera_type=fields.Selection([('Dipinto','Dipinto'),('Scultura','Scultura')], string="Tipologia")
    exclusive=fields.Boolean(string="Exclusive")
    opera_image=fields.Image(string="immagine", max_width=100, max_height=100)
    opera_description=fields.Char(string="Descrizione")
    esposizione=fields.Char(string="Esposizione")

    @api.model
    def create(self, vals):
        if vals.get('idcode', 'New') == 'New':
            vals['idcode']=self.env['ir.sequence'].next_by_code(
           'galleria_opera.code') or 'New'
        result=super(galleria_opera, self).create(vals)
        return result 
        
