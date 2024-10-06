from entities.Product.ProductPriceEntity import ProductPriceEntity
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum
from services.Service import Service


class ProductPriceService(Service):

    def format(self, price: ProductPriceEntity):
        integer_part = price.value // (10 ** price.currency.decimal_places)
        decimal_part = price.value % (10 ** price.currency.decimal_places)
        symbol = price.currency.symbol
        separator = price.currency.separator
        decimal_places = price.currency.decimal_places

        if price.currency.symbol_position == CurrencySymbolPositionEnum.BEFORE:
            return f'{symbol}{integer_part}{separator}{decimal_part:0>{decimal_places}}'
        elif price.currency.symbol_position == CurrencySymbolPositionEnum.AFTER:
            return f'{integer_part}{separator}{decimal_part:0>{decimal_places}}{symbol}'
