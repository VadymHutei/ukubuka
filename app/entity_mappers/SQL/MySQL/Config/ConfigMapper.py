from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class ConfigMapper(MySQLEntityMapper):

    def __init__(self):
        super().__init__(
            'config',
            'conf',
            [
                'id',
                'code',
                'value',
                'created_at',
                'updated_at',
            ],
            [
                'code',
                'value',
                'created_at',
                'updated_at',
            ],
            {
                'id': MapperFieldTypes.INT,
            },
        )
