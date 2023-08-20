from abc import ABC, abstractmethod

from entities.Product.ProductEntity import ProductEntity


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> ProductEntity|None:
        pass