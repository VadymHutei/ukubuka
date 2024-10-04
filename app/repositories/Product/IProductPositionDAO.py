from abc import ABC, abstractmethod


class IProductPositionDAO(ABC):

    @abstractmethod
    def find(self, product_position_id: int, only_active: bool) -> dict | None:
        pass

    @abstractmethod
    def find_ids_by_product_id(self, product_id: int, only_active: bool) -> list:
        pass
