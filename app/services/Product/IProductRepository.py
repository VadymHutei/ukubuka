from abc import ABC, abstractmethod

from entities.Product.ProductEntity import ProductEntity


class IProductRepository(ABC):

    @abstractmethod
    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        pass
