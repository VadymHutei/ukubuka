from flask import current_app as app

from entities.Currency.CurrencyEntity import CurrencyEntity
from repositories.Currency.ICurrencyDAO import ICurrencyDAO
from repositories.Repository import Repository
from repositories.builders.Currency.CurrencyBuilder import CurrencyBuilder
from repositories.builders.Currency.CurrencyBuilderParams import CurrencyBuilderParams
from repositories.stores.Currency.CurrencyStore import CurrencyStore


class CurrencyRepository(Repository):

    def __init__(self, currency_dao: ICurrencyDAO, currency_store: CurrencyStore, currency_builder: CurrencyBuilder):
        self._currency_dao = currency_dao
        self._currency_store = currency_store
        self._currency_builder = currency_builder

    def find(self, currency_id: int, only_active: bool) -> CurrencyEntity | None:
        use_store = app.config['USE_ENTITY_STORE']
        store_key = CurrencyStore.key_for(currency_id)

        if use_store and self._currency_store.has(store_key):
            currency = self._currency_store.get(store_key)
            return None if only_active and not currency.is_active else currency

        currency_builder_params = CurrencyBuilderParams(only_active=only_active)
        currency = self._currency_builder.build(currency_id, currency_builder_params)

        if currency is None:
            return None

        if use_store:
            self._currency_store.add(store_key, currency)

        return None if only_active and not currency.is_active else currency

    def find_by_code(self, currency_code: str, only_active: bool) -> CurrencyEntity | None:
        currency_id = self._currency_dao.find_id_by_code(currency_code)

        if currency_id is None:
            return None

        return self.find(currency_id, only_active)
