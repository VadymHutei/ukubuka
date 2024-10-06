from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum


@dataclass
class CurrencyEntity(Entity):

    code: str
    symbol: str
    symbol_position: CurrencySymbolPositionEnum
    separator: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None
