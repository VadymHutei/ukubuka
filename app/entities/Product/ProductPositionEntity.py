from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class ProductPositionEntity(Entity):

    SKU: int
    slug: str
    product_id: int
    is_active: bool
    created_at: datetime

    name: str | None = None
    description: str | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
