from entities.Product.ProductTextEntity import ProductTextEntity
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
        'id': int,
        'product_id': int,
        'language_id': int,
    }