from dataclasses import dataclass
from entities.Currency.CurrencyEntity import CurrencyEntity

from entities.IEntity import IEntity


@dataclass
class SKUPriceEntity(IEntity):

        id: int
        sku_id: int
        currency_id: int
        value: int
        created_at: str
        updated_at: str

        currency: CurrencyEntity | None = None