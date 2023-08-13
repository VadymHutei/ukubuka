from dataclasses import dataclass

from entities.CurencyEntity import CurencyEntity


@dataclass
class PriceEntity:

    id: int
    value: int
    currency: CurencyEntity