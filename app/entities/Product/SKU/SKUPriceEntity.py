from dataclasses import dataclass
from typing import Optional
from entities.Currency.CurrencyEntity import CurrencyEntity

from entities.Entity import Entity


@dataclass
class SKUPriceEntity(Entity):

        id: int
        sku_id: int
        currency_id: int
        value: int
        created_at: str
        updated_at: str

        currency: Optional[CurrencyEntity] = None