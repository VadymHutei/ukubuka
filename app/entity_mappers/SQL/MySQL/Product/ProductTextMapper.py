from entities.Product.ProductTextEntity import ProductTextEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class ProductTextMapper(MySQLEntityMapper):

    _ENTITY_CLASS = ProductTextEntity

    _TABLE = 'product_text'

    _TABLE_PREFIX = 'prd_t'

    _FIELDS = [
        'id',
        'product_id',
        'language_id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperFieldTypes.INT,
        'product_id': MapperFieldTypes.INT,
        'language_id': MapperFieldTypes.INT,
    }