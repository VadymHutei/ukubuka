from entities.Config.ConfigEntity import ConfigEntity
from repositories.MapperCast import MapperCast
from repositories.SQL.SQLEntityMapper import SQLEntityMapper


class ConfigMapper(SQLEntityMapper):

    _ENTITY_CLASS = ConfigEntity

    _TABLE = 'config'

    _TABLE_PREFIX = 'conf'

    _FIELDS = [
        'id',
        'code',
        'value',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperCast.INT,
    }