from entities.Page.PageEntity import PageEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class PageMapper(MySQLEntityMapper):

    _ENTITY_CLASS = PageEntity

    _TABLE = 'page'

    _TABLE_PREFIX = 'pg'

    _DATA_FIELDS = [
        'id',
        'code',
        'template',
        'layout',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _FILLABLE_FIELDS = [
        'code',
        'template',
        'layout',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'is_active': MapperFieldTypes.BOOL,
    }