from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class CurrencyEntity:

    id: int
    code: str
    symbol: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]