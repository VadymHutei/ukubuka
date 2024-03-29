from entities.Currency.CurrencyEntity import CurrencyEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class CurrencyMapper(MySQLEntityMapper):

    _ENTITY_CLASS = CurrencyEntity

    _TABLE = 'currency'

    _TABLE_PREFIX = 'cur'

    _DATA_FIELDS = [
        'id',
        'code',
        'symbol',
        'symbol_position',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _FIELD_TYPES = {
        'id': MapperFieldTypes.INT,
        'is_active': MapperFieldTypes.BOOL,
    }