
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.sale_shop.tests import SaleShopCompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase


class SaleShopTradeInfoTestCase(SaleShopCompanyTestMixin, ModuleTestCase):
    'Test SaleShopTradeInfo module'
    module = 'sale_shop_trade_info'


del ModuleTestCase
