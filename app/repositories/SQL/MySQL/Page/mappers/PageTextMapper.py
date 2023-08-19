from repositories.MapperCast import MapperCast
from repositories.SQL.SQLMapper import SQLMapper
from entities.Page.PageTextEntity import PageTextEntity


class PageTextMapper(SQLMapper):

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
        'id': MapperCast.int,
        'page_id': MapperCast.int,
        'language_id': MapperCast.int,
    }