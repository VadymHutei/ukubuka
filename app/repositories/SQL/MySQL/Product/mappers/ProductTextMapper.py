from entities.Product.ProductTextEntity import ProductTextEntity
from repositories.MapperCast import MapperCast
from repositories.SQL.SQLMapper import SQLMapper


class ProductTextMapper(SQLMapper):

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
        'id': MapperCast.int,
        'product_id': MapperCast.int,
        'language_id': MapperCast.int,
    }