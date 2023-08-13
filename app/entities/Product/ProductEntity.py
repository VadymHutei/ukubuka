from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from entities.Entity import Entity
from entities.Product.ProductTextEntity import ProductTextEntity
from entities.PriceEntity import PriceEntity
from exceptions.ProductException import ProductException


@dataclass
class ProductEntity(Entity):

    id: int
    code: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    _text: Optional[ProductTextEntity] = None
    _price: Optional[PriceEntity] = None

    @property
    def name(self):
        if self._text:
            return self._text.name
        else:
            raise ProductException('Product text data is not set')

    @property
    def description(self)-> str:
        if self._text:
            return self._text.description
        else:
            raise ProductException('Product text data is not set')

    @property
    def price(self) -> PriceEntity:
        if self._price:
            return self._price
        else:
            raise ProductException('Product price data is not set')