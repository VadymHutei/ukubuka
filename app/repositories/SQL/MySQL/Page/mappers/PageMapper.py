from repositories.SQL.SQLMapper import SQLMapper
from repositories.MapperCast import MapperCast
from entities.Page.PageEntity import PageEntity
from repositories.SQL.MySQL.Page.mappers.PageTextMapper import PageTextMapper


class PageMapper(SQLMapper):

    _ENTITY_CLASS = PageEntity

    _TABLE = 'page'

    _TABLE_PREFIX = 'pg'

    _FIELDS = [
        'id',
        'code',
        'template',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperCast.int,
        'is_active': MapperCast.bool,
    }

    _ENTITIES = {
        'text': PageTextMapper,
    }