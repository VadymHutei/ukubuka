from abc import ABC, abstractmethod


class IProductPriceDAO(ABC):

    @abstractmethod
    def find(self, product_price_id: int) -> dict | None:
        pass

    @abstractmethod
    def find_by_product_id_and_currency_id(self, product_id: int, currency_id: int) -> dict | None:
        pass

    @abstractmethod
    def find_id_by_product_id_and_currency_id(self, product_id: int, currency_id: int) -> int | None:
        pass
