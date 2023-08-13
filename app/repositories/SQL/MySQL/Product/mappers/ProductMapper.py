from entities.Product.ProductEntity import ProductEntity
from repositories.SQL.SQLMapper import SQLMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper


class ProductMapper(SQLMapper):

    _ENTITY_CLASS = ProductEntity

    _TABLE = 'product'

    _TABLE_PREFIX = 'p'

    _FIELDS = [
        'id',
        'code',
        'is_active',
        'created_at',
        'updated_at',
        'deleted_at',
    ]

    _CAST = {
        'id': int,
        'is_active': bool,
    }

    _ENTITIES = {
        'text': ProductTextMapper,
    }