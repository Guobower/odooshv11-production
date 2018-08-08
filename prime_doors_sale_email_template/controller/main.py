# -*- coding: utf-8 -*-

import base64

from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortal(CustomerPortal):
    
    @http.route(['/my/quotes/accept'], type='json', auth="public", website=True)
    def portal_quote_accept(self, res_id, access_token=None, partner_name=None, signature=None):
        res = super(CustomerPortal, self).(res_id, access_token partner_name, signature)
        if res_id:
            template_id = request.env['ir.model.data'].sudo().xmlid_to_object('prime_doors_sale_email_template.email_template_edi_sale_quote_acknowledgement')
            template_id.send_mail(res_id, True)
        return res
        