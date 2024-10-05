from dataclasses import dataclass, field
from datetime import datetime

from entities.Entity import Entity
from entities.Product.ProductPriceEntity import ProductPriceEntity


@dataclass
class ProductEntity(Entity):

    slug: str
    is_active: bool
    created_at: datetime

    name: str | None = None
    description: str | None = None
    price: ProductPriceEntity | None = None
    positions: dict = field(default_factory=dict)
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
