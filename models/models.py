"""."""
# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools.amount_to_text_en import english_number


class AccountVoucher(models.Model):
    """."""

    _inherit = 'account.voucher'

    def amount_to_text(self, amount, currency='naira'):
        """Convert anount to text format."""
        number = '%.2f' % float(amount)
        units_name = currency
        list = str(number).split('.')
        start_word = english_number(int(list[0]))
        end_word = english_number(int(list[1]))
        cents_number = int(list[1])
        cents_name = (cents_number > 1) and 'Kobo' or 'kobo'
        return ' '.join(filter(None, [start_word, units_name, (start_word or units_name) and (end_word or cents_name) and 'and', end_word, cents_name]))
