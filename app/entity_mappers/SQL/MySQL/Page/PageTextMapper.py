from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLTextEntityMapper import MySQLTextEntityMapper


class PageTextMapper(MySQLTextEntityMapper):

    def __init__(self):
        super().__init__(
            'page_text',
            'pg_t',
            [
                'id',
                'page_id',
                'language_id',
                'title',
                'created_at',
                'updated_at',
            ],
            [
                'page_id',
                'language_id',
                'title',
                'created_at',
                'updated_at',
            ],
            'page_id',
            {
                'id': MapperFieldTypes.INT,
                'page_id': MapperFieldTypes.INT,
                'language_id': MapperFieldTypes.INT,
            },
        )
