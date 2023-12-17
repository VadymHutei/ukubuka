from entities.Page.PageTranslationEntity import PageTranslationEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class PageTextMapper(MySQLEntityMapper):

    _ENTITY_CLASS = PageTranslationEntity

    _TABLE = 'page_text'

    _TABLE_PREFIX = 'pg_t'

    _DATA_FIELDS = [
        'id',
        'page_id',
        'language_id',
        'title',
        'created_at',
        'updated_at',
    ]

    _FILLABLE_FIELDS = [
        'page_id',
        'language_id',
        'title',
        'created_at',
        'updated_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'page_id': MapperFieldTypes.INT,
        'language_id': MapperFieldTypes.INT,
    }