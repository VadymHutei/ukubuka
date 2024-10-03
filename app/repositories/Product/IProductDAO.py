from abc import abstractmethod, ABC


class IProductDAO(ABC):

    @abstractmethod
    def find(self, product_id: int) -> dict | None:
        pass

    @abstractmethod
    def find_id_by_slug(self, product_slug: str) -> int | None:
        pass
