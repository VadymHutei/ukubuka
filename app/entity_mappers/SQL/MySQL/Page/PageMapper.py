from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class PageMapper(MySQLEntityMapper):

    def __init__(self):
        super().__init__(
            'page',
            'pg',
            (
                'id',
                'code',
                'template',
                'layout',
                'is_active',
                'created_at',
                'updated_at',
            ),
            (
                'code',
                'template',
                'layout',
                'is_active',
                'created_at',
                'updated_at',
            ),
            {
                'id': MapperFieldTypes.INT,
                'is_active': MapperFieldTypes.BOOL,
            },
        )
