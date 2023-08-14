from repositories.SQL.SQLMapper import SQLMapper
from entities.Product.ProductPriceEntity import ProductPriceEntity
from repositories.SQL.MySQL.Currency.CurrencyMapper import CurrencyMapper


class ProductPriceMapper(SQLMapper):

    _ENTITY_CLASS = ProductPriceEntity

    _TABLE = 'product_price'

    _TABLE_PREFIX = 'prd_prc'

    _FIELDS = [
        'id',
        'product_id',
        'currency_id',
        'value',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': int,
        'product_id': int,
        'currency_id': int,
        'value': int,
    }

    _ENTITIES = {
        'currency': CurrencyMapper
    }