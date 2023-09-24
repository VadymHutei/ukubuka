from entities.Catalog.CatalogTextEntity import CatalogTextEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class CatalogTextMapper(MySQLEntityMapper):

    _ENTITY_CLASS = CatalogTextEntity

    _TABLE = 'catalog_text'

    _TABLE_PREFIX = 'ctlg_txt'

    _DATA_FIELDS = [
        'id',
        'catalog_id',
        'language_id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'catalog_id': MapperFieldTypes.INT,
        'language_id': MapperFieldTypes.INT,
    }