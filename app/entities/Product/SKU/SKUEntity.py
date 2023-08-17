from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from entities.Entity import Entity
from entities.Product.SKU.SKUTextEntity import SKUTextEntity


@dataclass
class SKUEntity(Entity):

    id: int
    sku: int
    product_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    text: Optional[SKUTextEntity] = None
    price: Optional[SKUPrice] = None