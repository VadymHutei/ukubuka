from abc import ABC, abstractmethod
from typing import Optional

from entities.Product.ProductEntity import ProductEntity


class ProductRepository(ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> Optional[ProductEntity]:
        pass