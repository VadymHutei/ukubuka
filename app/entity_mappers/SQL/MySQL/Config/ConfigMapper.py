from entities.Config.ConfigEntity import ConfigEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class ConfigMapper(MySQLEntityMapper):

    _ENTITY_CLASS = ConfigEntity

    _TABLE = 'config'

    _TABLE_PREFIX = 'conf'

    _DATA_FIELDS = [
        'id',
        'code',
        'value',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperFieldTypes.INT,
    }