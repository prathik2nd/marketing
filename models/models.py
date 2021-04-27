# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api



class marketing(models.Model):
    _name = 'marketing.marketing'
    _description = 'marketing.marketing'

    name = fields.Char('Name')
    appdate = fields.Char('Appointment Date')
    state = fields.Selection([
       ('draft','Draft'),
       ('confirm','Confirm'),       
       ('cancel','Cancel'),
    ],string='Status', readonly=True, default='draft')


    def btnAction(self):
        self.appdate = datetime.datetime.now()
    
    def actionState(self):
        print('state')

    