from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class LanguageMapper(MySQLEntityMapper):

    def __init__(self):
        super().__init__(
            'language',
            'lng',
            (
                'id',
                'code',
                'name',
                'is_active',
                'created_at',
                'updated_at',
                'deleted_at',
            ),
            (
                'code',
                'name',
                'is_active',
                'created_at',
                'updated_at',
                'deleted_at',
            ),
            {
                'id': MapperFieldTypes.INT,
                'is_active': MapperFieldTypes.BOOL,
            },
        )
