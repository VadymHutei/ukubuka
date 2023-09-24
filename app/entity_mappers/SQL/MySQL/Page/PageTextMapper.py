from entities.Page.PageTextEntity import PageTextEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class PageTextMapper(MySQLEntityMapper):

    _ENTITY_CLASS = PageTextEntity

    _TABLE = 'page_text'

    _TABLE_PREFIX = 'pg_t'

    _FIELDS = [
        'id',
        'page_id',
        'language_id',
        'title',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperFieldTypes.INT,
        'page_id': MapperFieldTypes.INT,
        'language_id': MapperFieldTypes.INT,
    }