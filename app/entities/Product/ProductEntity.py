from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class ProductEntity(Entity):

    slug: str
    name: str
    is_active: bool
    created_at: datetime

    description: str | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
