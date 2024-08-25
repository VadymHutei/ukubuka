from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class CatalogTextEntity(Entity):

    catalog_id: int
    language_id: int
    name: str
    description: str
    created_at: datetime

    updated_at: datetime | None = None
