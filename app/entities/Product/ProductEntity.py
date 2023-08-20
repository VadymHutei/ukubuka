from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Product.ProductPriceEntity import ProductPriceEntity
from entities.Product.ProductTextEntity import ProductTextEntity
from exceptions.entities_exception.ProductException import ProductException


@dataclass
class ProductEntity(Entity):

    id: int
    code: str
    is_active: bool
    created_at: datetime
    updated_at: datetime|None
    deleted_at: datetime|None

    text: ProductTextEntity|None = None
    price: ProductPriceEntity|None = None

    @property
    def name(self) -> str:
        if self.text:
            return self.text.name
        else:
            raise ProductException('Product text data is not set')

    @property
    def description(self)-> str:
        if self.text:
            return self.text.description
        else:
            raise ProductException('Product text data is not set')