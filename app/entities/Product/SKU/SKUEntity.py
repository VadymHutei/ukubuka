from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Product.SKU.SKUTextEntity import SKUTextEntity


@dataclass
class SKUEntity(Entity):

    id: int
    sku: int
    product_id: int
    created_at: datetime
    updated_at: datetime|None

    text: SKUTextEntity|None = None