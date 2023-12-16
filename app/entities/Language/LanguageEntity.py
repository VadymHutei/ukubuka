from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class LanguageEntity(Entity):

    code: str
    name: str
    is_active: bool
    created_at: datetime

    id: int | None = None
    updated_at: datetime | None = None