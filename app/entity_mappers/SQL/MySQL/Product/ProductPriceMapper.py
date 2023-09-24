from entities.Product.ProductPriceEntity import ProductPriceEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.Currency.CurrencyMapper import CurrencyMapper
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class ProductPriceMapper(MySQLEntityMapper):

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
        'id': MapperFieldTypes.INT,
        'product_id': MapperFieldTypes.INT,
        'currency_id': MapperFieldTypes.INT,
        'value': MapperFieldTypes.INT,
    }

    _ENTITIES = {
        'currency': CurrencyMapper,
    }