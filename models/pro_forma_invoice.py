from odoo import models,fields,api
from datetime import datetime
import convert_numbers


from uuid import uuid4
import qrcode
import base64
import logging

from lxml import etree

class ProFormaInvoice(models.Model):
    _inherit = 'pro.forma.invoice'

    def ar_total_tax(self):
        value = self.amount_untaxed * 0.15
        before, after = str('{:.2f}'.format(value)).split('.')
        before_int = int(before)
        after_int = after
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar


    def amount_total_arabic(self):
        value = self.amount_total
        value = '%.2f' % value
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

