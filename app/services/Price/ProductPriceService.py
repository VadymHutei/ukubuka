from entities.Product.ProductPriceEntity import ProductPriceEntity
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum
from services.Service import Service


class ProductPriceService(Service):

    def format(self, price: ProductPriceEntity):
        if price.currency.symbol_position == CurrencySymbolPositionEnum.BEFORE:
            return f'{price.currency.symbol}{price.value // 100}{price.currency.separator}{price.value % 100:02}'
        elif price.currency.symbol_position == CurrencySymbolPositionEnum.AFTER:
            return f'{price.value // 100}{price.currency.separator}{price.value % 100:02}{price.currency.symbol}'
