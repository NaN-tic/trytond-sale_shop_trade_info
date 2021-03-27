# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import shop

def register():
    Pool.register(
        shop.Shop,
        module='sale_shop_trade_info', type_='model')
