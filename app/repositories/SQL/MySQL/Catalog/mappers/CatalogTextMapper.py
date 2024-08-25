from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLTextEntityMapper import MySQLTextEntityMapper


class CatalogTextMapper(MySQLTextEntityMapper):

    def __init__(self):
        super().__init__(
            'catalog_text',
            'ct_t',
            (
                'id',
                'catalog_id',
                'language_id',
                'name',
                'description',
                'created_at',
                'updated_at',
            ),
            (
                'catalog_id',
                'language_id',
                'name',
                'description',
                'created_at',
                'updated_at',
            ),
            (
                'title',
            ),
            'catalog_id',
            {
                'id': MapperFieldTypes.INT,
                'catalog_id': MapperFieldTypes.INT,
                'language_id': MapperFieldTypes.INT,
            },
        )
