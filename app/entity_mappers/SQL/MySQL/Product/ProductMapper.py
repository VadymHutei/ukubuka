from entities.Product.ProductEntity import ProductEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper
from entity_mappers.SQL.MySQL.Product.ProductPriceMapper import ProductPriceMapper
from entity_mappers.SQL.MySQL.Product.ProductTextMapper import ProductTextMapper


class ProductMapper(MySQLEntityMapper):

    _ENTITY_CLASS = ProductEntity

    _TABLE = 'product'

    _TABLE_PREFIX = 'prd'

    _DATA_FIELDS = [
        'id',
        'code',
        'is_active',
        'created_at',
        'updated_at',
        'deleted_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'is_active': MapperFieldTypes.BOOL,
    }

    _NESTED_ENTITY_MAPPERS = {
        'text': ProductTextMapper,
        'price': ProductPriceMapper
    }