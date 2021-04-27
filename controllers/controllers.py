# -*- coding: utf-8 -*-
from odoo import http


class Marketing(http.Controller):
    @http.route('/marketing/marketing/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/marketing/marketing/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('marketing.listing', {
            'root': '/marketing/marketing',
            'objects': http.request.env['marketing.marketing'].search([]),
        })

    @http.route('/marketing/marketing/objects/<model("marketing.marketing"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('marketing.object', {
            'object': obj
        })
