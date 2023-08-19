from entities.Page.PageEntity import PageEntity
from repositories.MapperCast import MapperCast
from repositories.SQL.MySQL.Page.mappers.PageTextMapper import PageTextMapper
from repositories.SQL.SQLEntityMapper import SQLEntityMapper


class PageMapper(SQLEntityMapper):

    _ENTITY_CLASS = PageEntity

    _TABLE = 'page'

    _TABLE_PREFIX = 'pg'

    _FIELDS = [
        'id',
        'code',
        'template',
        'layout',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperCast.INT,
        'is_active': MapperCast.BOOL,
    }

    _ENTITIES = {
        'text': PageTextMapper,
    }