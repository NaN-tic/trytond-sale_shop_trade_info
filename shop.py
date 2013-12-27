# This file is part sale_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Shop']
__metaclass__ = PoolMeta


class Shop:
    __name__ = 'sale.shop'

    logo = fields.Binary('Logo')
    address = fields.Many2One('party.address', 'Address')
    lang = fields.Many2One("ir.lang", 'Language')
    company_trade_name = fields.Char('Company Trade Name')
