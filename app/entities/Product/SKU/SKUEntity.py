from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Product.SKU.SKUTextEntity import SKUTextEntity


@dataclass
class SKUEntity(Entity):

    sku: int
    product_id: int
    created_at: datetime
    updated_at: datetime | None = None

    text: SKUTextEntity | None = None