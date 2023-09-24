from entities.Currency.CurrencyEntity import CurrencyEntity
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper


class CurrencyMapper(MySQLEntityMapper):

    _ENTITY_CLASS = CurrencyEntity

    _TABLE = 'currency'

    _TABLE_PREFIX = 'cur'

    _FIELDS = [
        'id',
        'code',
        'symbol',
        'symbol_position',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperFieldTypes.INT,
        'is_active': MapperFieldTypes.BOOL,
    }