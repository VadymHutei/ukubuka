from entities.Catalog.CatalogEntity import CatalogEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class CatalogMapper(MySQLEntityMapper):

    _ENTITY_CLASS = CatalogEntity

    _TABLE = 'catalog'

    _TABLE_PREFIX = 'ctlg'

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