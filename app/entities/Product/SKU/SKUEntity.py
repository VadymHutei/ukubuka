from dataclasses import dataclass
from datetime import datetime

from entities.IEntity import IEntity
from entities.Product.SKU.SKUTextEntity import SKUTextEntity


@dataclass
class SKUEntity(IEntity):

    id: int
    sku: int
    product_id: int
    created_at: datetime
    updated_at: datetime | None = None

    text: SKUTextEntity | None = None