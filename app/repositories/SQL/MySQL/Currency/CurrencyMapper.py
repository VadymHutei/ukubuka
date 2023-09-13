from repositories.MapperCast import MapperCast
from repositories.SQL.SQLEntityMapper import SQLEntityMapper
from entities.Currency.CurrencyEntity import CurrencyEntity


class CurrencyMapper(SQLEntityMapper):

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
        'id': MapperCast.INT,
        'is_active': MapperCast.BOOL,
    }