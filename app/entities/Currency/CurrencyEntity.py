from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class CurrencyEntity(Entity):

    id: int
    code: str
    symbol: str
    is_active: bool
    created_at: datetime
    updated_at: datetime|None