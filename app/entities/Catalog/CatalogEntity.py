from dataclasses import dataclass
from datetime import datetime

from entities.IEntity import IEntity


@dataclass
class CatalogEntity(IEntity):

    id: int
    code: str
    is_active: bool
    created_at: datetime
    updated_at: datetime|None = None
    deleted_at: datetime|None = None