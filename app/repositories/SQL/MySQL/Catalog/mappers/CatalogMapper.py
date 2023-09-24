from entities.Catalog.CatalogEntity import CatalogEntity
from repositories.MapperCast import MapperCast
from repositories.SQL.SQLEntityMapper import SQLEntityMapper


class CatalogMapper(SQLEntityMapper):

    _ENTITY_CLASS = CatalogEntity

    _TABLE = 'catalog'

    _TABLE_PREFIX = 'ctlg'

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