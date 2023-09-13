from entities.Product.ProductEntity import ProductEntity
from repositories.MapperCast import MapperCast
from repositories.SQL.MySQL.Product.mappers.ProductPriceMapper import ProductPriceMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from repositories.SQL.SQLEntityMapper import SQLEntityMapper


class ProductMapper(SQLEntityMapper):

    _ENTITY_CLASS = ProductEntity

    _TABLE = 'product'

    _TABLE_PREFIX = 'prd'

    _FIELDS = [
        'id',
        'code',
        'is_active',
        'created_at',
        'updated_at',
        'deleted_at',
    ]

    _CAST = {
        'id': MapperCast.INT,
        'is_active': MapperCast.BOOL,
    }

    _ENTITIES = {
        'text': ProductTextMapper,
        'price': ProductPriceMapper
    }