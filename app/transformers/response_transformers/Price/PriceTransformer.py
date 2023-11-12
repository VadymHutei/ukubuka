from custom_types.Price import Price
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum
from transformers.response_transformers.ResponseTransformer import ResponseTransformer


class PriceTransformer(ResponseTransformer):

    @staticmethod
    def transform(price: Price) -> str:
        print(price)
        delimiter = ','
        decimal_separator = '.'
        integer = f'{price.integer:{delimiter}}'
        fractional = f'{price.fractional:0{price._DIGITS}}'[:price._DIGITS]
        formated_price = f'{integer}{decimal_separator}{fractional}'
        match price.currency.symbol_position:
            case CurrencySymbolPositionEnum.BEFORE:
                return f'{price.currency.symbol}{formated_price}'
            case CurrencySymbolPositionEnum.AFTER | _:
                return f'{formated_price}{price.currency.symbol}'