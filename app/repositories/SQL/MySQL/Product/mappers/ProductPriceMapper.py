from repositories.SQL.SQLMapper import SQLMapper
from repositories.MapperCast import MapperCast
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
        'id': MapperCast.int,
        'product_id': MapperCast.int,
        'currency_id': MapperCast.int,
        'value': MapperCast.int,
    }

    _ENTITIES = {
        'currency': CurrencyMapper
    }