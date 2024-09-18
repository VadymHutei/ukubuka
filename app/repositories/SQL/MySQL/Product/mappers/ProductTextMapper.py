from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLTextEntityMapper import MySQLTextEntityMapper


class ProductTextMapper(MySQLTextEntityMapper):

    def __init__(self):
        super().__init__(
            'product_text',
            'prd_t',
            (
                'id',
                'product_id',
                'language_id',
                'name',
                'description',
                'created_at',
                'updated_at',
            ),
            (
                'product_id',
                'language_id',
                'name',
                'description',
                'created_at',
                'updated_at',
            ),
            (
                'name',
                'description',
            ),
            'product_id',
            {
                'id': MapperFieldTypes.INT,
                'product_id': MapperFieldTypes.INT,
                'language_id': MapperFieldTypes.INT,
            },
        )
