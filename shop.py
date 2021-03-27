# This file is part sale_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Shop(metaclass=PoolMeta):
    __name__ = 'sale.shop'

    logo = fields.Binary('Logo')
    lang = fields.Many2One("ir.lang", 'Language')
    company_trade_name = fields.Char('Company Trade Name')
    phone = fields.Char('Phone')
    website = fields.Char('Website')
    email = fields.Char('E-Mail')
