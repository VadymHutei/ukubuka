from entities.Currency.CurrencyEntity import CurrencyEntity
from repositories.stores.Store import Store


class CurrencyStore(Store[CurrencyEntity]):

    @staticmethod
    def key_for(currency_id: int) -> str:
        return f'{currency_id}'
