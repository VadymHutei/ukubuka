from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class CatalogEntity(Entity):

    code: str
    is_active: bool
    name: str
    created_at: datetime

    description: str | None = None
    updated_at: datetime | None = None
