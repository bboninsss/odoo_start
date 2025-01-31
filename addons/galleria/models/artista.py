# -*- coding: utf-8 -*-

from odoo import models, fields, api 
from datetime import date


class artista(models.Model):
    _name="artista"
    _description="artista"
    _recname="code"

    code=fields.Char(string="Codice Fiscale", required=True)
    surname=fields.Char(string="Cognome")
    name=fields.Char(string="Nome")
    place=fields.Char(string="Luogo di nascita")
    birth=fields.Date(string="Data di nascita")
    telefono=fields.Char(string="Telefono")
    email=fields.Char(string="E-mail")
    activity=fields.Boolean(string="In attività")
    iban=fields.Char(string="Iban")

    def name_get(self):
        result=[]
        for rec in self:
            name='' + rec.name + '  ' + rec.surname
            result.append((rec.id, name))
        return result 