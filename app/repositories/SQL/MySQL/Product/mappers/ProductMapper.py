from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class ProductMapper(MySQLEntityMapper):

    def __init__(self):
        super().__init__(
            'product',
            'prd',
            (
                'id',
                'slug',
                'is_active',
                'created_at',
                'updated_at',
                'deleted_at',
            ),
            (
                'slug',
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
