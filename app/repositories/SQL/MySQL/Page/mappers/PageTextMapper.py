from repositories.MapperCast import MapperCast
from repositories.SQL.SQLEntityMapper import SQLEntityMapper
from entities.Page.PageTextEntity import PageTextEntity


class PageTextMapper(SQLEntityMapper):

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
        'id': MapperCast.INT,
        'page_id': MapperCast.INT,
        'language_id': MapperCast.INT,
    }