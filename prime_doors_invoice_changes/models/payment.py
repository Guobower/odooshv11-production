# -*- coding: utf-8 -*-
##########################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
##########################################################################

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.multi
    def post(self):
        res = super(AccountPayment, self).post()
        for rec in self:
            for invoice in rec.invoice_ids:
                for vals in invoice._get_payments_vals():
                    if vals.get('invoice_id'):
                        rec.invoice_ids = [(4, vals.get('invoice_id'))]
        return res
