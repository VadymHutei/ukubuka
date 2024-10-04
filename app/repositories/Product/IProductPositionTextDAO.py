from abc import ABC, abstractmethod


class IProductPositionTextDAO(ABC):

    @abstractmethod
    def find_by_product_position_id_and_language_id(self, product_position_id: int, language_id: int) -> dict | None:
        pass
