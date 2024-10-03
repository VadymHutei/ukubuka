from abc import ABC, abstractmethod


class IProductTextDAO(ABC):

    @abstractmethod
    def find_by_product_id_and_language_id(self, product_id: int, language_id: int) -> dict | None:
        pass
