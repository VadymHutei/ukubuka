from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from entities.Entity import Entity


@dataclass
class ProductPriceEntity(Entity):

    id: int
    product_id: int
    currency_id: int
    value: int
    created_at: datetime
    updated_at: Optional[datetime]

    currency: Optional[str] = None