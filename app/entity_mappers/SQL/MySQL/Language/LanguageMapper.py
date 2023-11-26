from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class LanguageMapper(MySQLEntityMapper):

    _ENTITY_CLASS = LanguageEntity

    _TABLE = 'language'

    _TABLE_PREFIX = 'lng'

    _DATA_FIELDS = [
        'id',
        'code',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _FILLABLE_FIELDS = [
        'code',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'is_active': MapperFieldTypes.BOOL,
    }