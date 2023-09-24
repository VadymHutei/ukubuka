from dataclasses import dataclass
from datetime import datetime

from entities.IEntity import IEntity
from enums.CurrencySymbolPositionEnum import CurrencySymbolPositionEnum


@dataclass
class CurrencyEntity(IEntity):

    id: int
    code: str
    symbol: str
    symbol_position: CurrencySymbolPositionEnum
    is_active: bool
    created_at: datetime
    updated_at: datetime|None = None