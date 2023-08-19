from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from entities.Entity import Entity


@dataclass
class LanguageEntity(Entity):

    id: int
    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None