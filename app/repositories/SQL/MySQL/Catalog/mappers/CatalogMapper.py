from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class CatalogMapper(MySQLEntityMapper):

    def __init__(self):
        super().__init__(
            'catalog',
            'ct',
            (
                'id',
                'code',
                'is_active',
                'created_at',
                'updated_at',
            ),
            (
                'code',
                'is_active',
                'created_at',
                'updated_at',
            ),
            {
                'id': MapperFieldTypes.INT,
                'is_active': MapperFieldTypes.BOOL,
            },
        )
