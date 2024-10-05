from entities.Currency.CurrencyEntity import CurrencyEntity
from repositories.Currency.CurrencyRepository import CurrencyRepository
from services.Service import Service


class CurrencyService(Service):

    def __init__(self, currency_repository: CurrencyRepository):
        self._currency_repository = currency_repository

    def find_by_code(self, currency_code: str, only_active: bool) -> CurrencyEntity | None:
        return self._currency_repository.find_by_code(currency_code, only_active)
