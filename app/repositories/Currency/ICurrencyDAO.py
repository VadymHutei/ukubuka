from abc import ABC, abstractmethod


class ICurrencyDAO(ABC):

    @abstractmethod
    def find(self, currency_id: int, only_active: bool) -> dict | None:
        pass

    @abstractmethod
    def find_by_code(self, currency_code: str, only_active: bool) -> dict | None:
        pass

    @abstractmethod
    def find_id_by_code(self, currency_code: str) -> int | None:
        pass
