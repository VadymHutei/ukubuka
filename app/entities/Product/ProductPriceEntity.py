from dataclasses import dataclass
from datetime import datetime
from entities.Currency.CurrencyEntity import CurrencyEntity

from entities.Entity import Entity


@dataclass
class ProductPriceEntity(Entity):

    product_id: int
    currency_id: int
    value: int
    created_at: datetime
    updated_at: datetime | None = None

    currency: CurrencyEntity | None = None