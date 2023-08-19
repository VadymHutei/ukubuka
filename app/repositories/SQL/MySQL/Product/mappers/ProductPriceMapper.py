from repositories.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.MapperCast import MapperCast
from entities.Product.ProductPriceEntity import ProductPriceEntity
from repositories.SQL.MySQL.Currency.CurrencyMapper import CurrencyMapper


class ProductPriceMapper(SQLEntityMapper):

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
        'id': MapperCast.INT,
        'product_id': MapperCast.INT,
        'currency_id': MapperCast.INT,
        'value': MapperCast.INT,
    }

    _ENTITIES = {
        'currency': CurrencyMapper
    }