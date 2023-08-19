from repositories.MapperCast import MapperCast
from repositories.SQL.SQLMapper import SQLMapper
from entities.Currency.CurrencyEntity import CurrencyEntity


class CurrencyMapper(SQLMapper):

    _ENTITY_CLASS = CurrencyEntity

    _TABLE = 'currency'

    _TABLE_PREFIX = 'cur'

    _FIELDS = [
        'id',
        'code',
        'symbol',
        'is_active',
        'created_at',
        'updated_at',
    ]

    _CAST = {
        'id': MapperCast.int,
        'is_active': MapperCast.bool,
    }