from entities.Currency.CurrencyEntity import CurrencyEntity
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum
from repositories.Currency.ICurrencyDAO import ICurrencyDAO
from repositories.builders.Builder import Builder
from repositories.builders.Currency.CurrencyBuilderParams import CurrencyBuilderParams


class CurrencyBuilder(Builder[CurrencyEntity]):

    def __init__(self, currency_dao: ICurrencyDAO):
        self._currency_dao = currency_dao

    def build(self, currency_id: int, params: CurrencyBuilderParams | None = None):
        currency = self._create_currency(currency_id, params.only_active)

        if currency is None:
            return None

        return currency

    def _create_currency(self, currency_id: int, only_active: bool) -> CurrencyEntity | None:
        currency_record = self._currency_dao.find(currency_id, only_active)

        if currency_record is None:
            return None

        return CurrencyEntity(
            id=currency_record['id'],
            code=currency_record['code'],
            symbol=currency_record['symbol'],
            symbol_position=CurrencySymbolPositionEnum(currency_record['symbol_position']),
            separator=currency_record['separator'],
            decimal_places=currency_record['decimal_places'],
            is_active=currency_record['is_active'],
            created_at=currency_record['created_at'],
            updated_at=currency_record['updated_at'],
        )
