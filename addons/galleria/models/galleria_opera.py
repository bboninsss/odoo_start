# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError


class galleria_opera(models.Model):
    _name="galleria_opera"
    _description="opera"
    _recname="name"

    idcode=fields.Char(string="CodiceID",required=True, readonly=True, default='New')
    name=fields.Char(string="Nome Opera", required=True)
    artista=fields.Many2one("artista", string="Artista")
    data=fields.Date(string="Data produzione")
    tipo_opera = fields.Selection([('dip', 'Dipinto'), ('scul', 'Scultura')], string="Tipologia")
    exclusive=fields.Selection([('base', 'Base'), ('exc', 'Exclusive')], default="base", string="Esclusività")
    opera_image=fields.Image(string="immagine", max_width=100, max_height=100)
    opera_description=fields.Text(string="Descrizione")
    esposizione=fields.Char(string="Esposizione")
    
    
    @api.model
    def create(self, vals):
        if vals.get('idcode', 'New') == 'New':
            vals['idcode']=self.env['ir.sequence'].next_by_code(
           'galleria_opera.code') or 'New'
        result=super(galleria_opera, self).create(vals)
        return result 
    
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            opera = self.env['galleria_opera'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if opera:
                raise ValidationError(_("Name %s Already Exists" % rec.name))
    
    # @api.onchange('tags')
    # def get_exc(self, vals):
    #     vals= {
    #     'exclusive':self.exclusive,
    #     'tags':self.tags
    #     }
    #     if vals.get['exclusive','True'] == 'True':
    #         vals['tags']=self.tags['exc']
    
    @api.model
    def get_tags(self):
        return self.env['galleria.galleria'].search([('name', 'in', ['base', 'exc'])]).ids
    tags = fields.Many2many('galleria.galleria', default=get_tags, string="tag")

       

    
    