from dataclasses import dataclass
from datetime import datetime

from entities.IEntity import IEntity


@dataclass
class LanguageEntity(IEntity):

    id: int
    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None