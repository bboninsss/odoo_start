# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class opera_profile(models.Model):
    _name="opera_profile"
    _description="opera"
    _recname="code"

    code=fields.Char(string="CodiceID", required=True, readonly=True, 
            default="New")
    name=fields._String (string="Nome Opera", required=True)
    autore=fields.string (string="Autore")
    data=fields.DATE_FORMAT(string="Data produzione")
    opera_type=fields.selection ([("pittura", "Quadro"),("scultura","Scultura")], string="Tipologia")
    opera_image=fields.image(string="immagine", max_width=200, max_height=200)
    opera_description=fields.html(string="Descrizione")
